from pathlib import Path
import sys

import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from backend.db import connect, init_db, log_event


def set_status(draft_id: int, status: str) -> None:
    with connect() as con:
        con.execute("update drafts set status = ? where id = ?", (status, draft_id))
        con.execute(
            "update approvals set status = ?, updated_at = current_timestamp where draft_id = ?",
            (status, draft_id),
        )
        log_event(con, f"approval.{status}", f"draft_id={draft_id}")
        con.commit()


def main() -> None:
    st.set_page_config(page_title="Approval Queue", layout="wide")
    st.title("Approval Queue")
    init_db()

    with st.expander("Request intake", expanded=True):
        with st.form("request-intake-form", clear_on_submit=True):
            title = st.text_input("Title", placeholder="예: 신규 업무 자동화")
            goal = st.text_area("Goal", placeholder="사용자가 이루고 싶은 업무 목표")
            context = st.text_area("Context", placeholder="기존 자료, 기존 프롬프트, 참고 링크")
            constraints = st.text_area("Constraints", placeholder="시간, 예산, 형식, 금지사항")
            submitted = st.form_submit_button("Save request")
            if submitted:
                if not title.strip() or not goal.strip():
                    st.error("Title and Goal are required.")
                else:
                    with connect() as con:
                        con.execute(
                            """
                            insert into intake_requests(title, goal, context, constraints, status)
                            values (?, ?, ?, ?, 'new')
                            """,
                            (title.strip(), goal.strip(), context.strip(), constraints.strip()),
                        )
                        log_event(con, "request_intake.created", title.strip())
                        con.commit()
                    st.success("Request saved.")

    with connect() as con:
        drafts = con.execute(
            """
            select d.id, d.body, d.status, r.title, r.goal
            from drafts d
            join intake_requests r on r.id = d.request_id
            order by d.created_at desc
            """
        ).fetchall()

    if not drafts:
        st.info("No drafts yet. Run `python backend/seed_input.py` and `python agents/task_agent.py`.")

    if drafts:
        for draft in drafts:
            with st.container(border=True):
                st.subheader(f"Draft #{draft['id']} - {draft['status']}")
                st.caption(f"{draft['title']} | {draft['goal']}")
                st.text_area("Draft body", draft["body"], height=240, key=f"body-{draft['id']}")
                col1, col2 = st.columns(2)
                if col1.button("Approve", key=f"approve-{draft['id']}"):
                    set_status(draft["id"], "approved")
                    st.rerun()
                if col2.button("Reject", key=f"reject-{draft['id']}"):
                    set_status(draft["id"], "rejected")
                    st.rerun()

    with connect() as con:
        requests = con.execute(
            """
            select id, title, goal, context, constraints, status, created_at
            from intake_requests
            order by created_at desc
            """
        ).fetchall()

    if requests:
        st.divider()
        st.subheader("Request intake log")
        for request in requests:
            with st.container(border=True):
                st.caption(f"{request['created_at']} | {request['status']}")
                st.write(f"**{request['title']}**")
                st.write(request["goal"])
                if request["context"]:
                    st.write(request["context"])
                if request["constraints"]:
                    st.write(request["constraints"])


if __name__ == "__main__":
    main()
