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

    with connect() as con:
        drafts = con.execute(
            """
            select d.id, d.body, d.status, o.customer_name, o.question
            from drafts d
            join orders o on o.id = d.order_id
            order by d.created_at desc
            """
        ).fetchall()

    if not drafts:
        st.info("No drafts yet. Run `python backend/seed_input.py` and `python agents/task_agent.py`.")
        return

    for draft in drafts:
        with st.container(border=True):
            st.subheader(f"Draft #{draft['id']} - {draft['status']}")
            st.caption(f"{draft['customer_name']} | {draft['question']}")
            st.text_area("Draft body", draft["body"], height=240, key=f"body-{draft['id']}")
            col1, col2 = st.columns(2)
            if col1.button("Approve", key=f"approve-{draft['id']}"):
                set_status(draft["id"], "approved")
                st.rerun()
            if col2.button("Reject", key=f"reject-{draft['id']}"):
                set_status(draft["id"], "rejected")
                st.rerun()


if __name__ == "__main__":
    main()
