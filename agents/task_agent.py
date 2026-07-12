from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from backend.db import connect, init_db, log_event


def build_draft(question: str, cards: str) -> str:
    return f"""카드 해석
{cards} 흐름은 지금 결론을 서두르기보다 상황을 차분히 확인해야 한다는 쪽에 가깝습니다.

종합 흐름
질문은 "{question}"입니다. 현재는 상대나 환경의 반응을 관찰하면서 선택지를 좁히는 단계입니다.

현실 조언
오늘 할 일은 하나입니다. 감정이 올라온 상태에서 긴 메시지를 보내기보다, 확인해야 할 사실을 한 문장으로 정리하세요.

확인 질문
지금 가장 확인하고 싶은 것은 상대의 마음인가요, 아니면 내가 다음 행동을 해도 되는 타이밍인가요?"""


def main() -> None:
    init_db()
    with connect() as con:
        order = con.execute(
            "select id, customer_name, question, cards from orders where status = 'new' order by id limit 1"
        ).fetchone()
        if not order:
            print("No new orders.")
            return

        draft = build_draft(order["question"], order["cards"])
        cur = con.execute(
            "insert into drafts(order_id, body, status) values (?, ?, 'pending')",
            (order["id"], draft),
        )
        con.execute("update orders set status = 'drafted' where id = ?", (order["id"],))
        con.execute(
            "insert into approvals(draft_id, status, reviewer_note) values (?, 'pending', '')",
            (cur.lastrowid,),
        )
        log_event(con, "task_agent.draft_created", f"draft_id={cur.lastrowid}")
        con.commit()
        print(f"Created draft #{cur.lastrowid} for {order['customer_name']}")


if __name__ == "__main__":
    main()
