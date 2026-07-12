from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from backend.db import connect, init_db, log_event


def main() -> None:
    init_db()
    with connect() as con:
        con.execute(
            "insert into orders(customer_name, question, cards) values (?, ?, ?)",
            ("sample-customer", "연락이 끊긴 상대에게 먼저 연락해도 될까요?", "Two of Cups, Four of Swords, Page of Cups"),
        )
        log_event(con, "seed.input_created", "sample task input")
        con.commit()
    print("Seeded one sample order.")


if __name__ == "__main__":
    main()
