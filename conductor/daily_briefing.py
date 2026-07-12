from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from backend.db import connect, init_db


def count_by_status(table: str) -> dict[str, int]:
    with connect() as con:
        rows = con.execute(f"select status, count(*) as count from {table} group by status").fetchall()
    return {row["status"]: row["count"] for row in rows}


def main() -> None:
    init_db()
    draft_counts = count_by_status("drafts")
    approval_counts = count_by_status("approvals")

    with connect() as con:
        logs = con.execute(
            "select event, detail, created_at from run_logs order by id desc limit 5"
        ).fetchall()

    print("# Daily Agent Team Briefing")
    print()
    print("## Drafts")
    print(f"- Pending: {draft_counts.get('pending', 0)}")
    print(f"- Approved: {draft_counts.get('approved', 0)}")
    print(f"- Rejected: {draft_counts.get('rejected', 0)}")
    print()
    print("## Approvals")
    print(f"- Pending: {approval_counts.get('pending', 0)}")
    print(f"- Approved: {approval_counts.get('approved', 0)}")
    print(f"- Rejected: {approval_counts.get('rejected', 0)}")
    print()
    print("## Recent Logs")
    for row in logs:
        print(f"- {row['created_at']} | {row['event']} | {row['detail']}")


if __name__ == "__main__":
    main()

