from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from backend.db import connect, init_db, log_event


def build_draft(title: str, goal: str, context: str, constraints: str) -> str:
    return f"""입력 요약
제목: {title}
목표: {goal}
배경: {context}
제약: {constraints}

작업 흐름
1. 입력 목표를 한 문장으로 다시 쓴다.
2. 기존 자료와 제약 조건을 기준으로 실행 순서를 정한다.
3. 바로 만들 수 있는 것과 나중에 붙일 것을 나눈다.

실행 조언
작게 시작하고, 한 단계가 끝날 때마다 검증한다.

확인 질문
이 목표를 먼저 자동화할지, 먼저 승인 큐를 붙일지, 아니면 먼저 문서 정리를 할지 정해 주세요."""


def main() -> None:
    init_db()
    with connect() as con:
        request = con.execute(
            """
            select id, title, goal, context, constraints
            from intake_requests
            where status = 'new'
            order by id
            limit 1
            """
        ).fetchone()
        if not request:
            print("No new requests.")
            return

        draft = build_draft(request["title"], request["goal"], request["context"], request["constraints"])
        cur = con.execute(
            "insert into drafts(request_id, body, status) values (?, ?, 'pending')",
            (request["id"], draft),
        )
        con.execute("update intake_requests set status = 'drafted' where id = ?", (request["id"],))
        con.execute(
            "insert into approvals(draft_id, status, reviewer_note) values (?, 'pending', '')",
            (cur.lastrowid,),
        )
        log_event(con, "task_agent.draft_created", f"draft_id={cur.lastrowid}")
        con.commit()
        print(f"Created draft #{cur.lastrowid} for {request['title']}")


if __name__ == "__main__":
    main()
