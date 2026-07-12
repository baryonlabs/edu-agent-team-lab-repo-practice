from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from backend.db import connect, init_db, log_event


def main() -> None:
    init_db()
    with connect() as con:
        con.execute(
            """
            insert into intake_requests(title, goal, context, constraints, status)
            values (?, ?, ?, ?, 'new')
            """,
            (
                "샘플 업무 요청",
                "사용자가 추가로 입력한 업무 목표를 Agent Team으로 실행해 보기",
                "기존 문서와 프롬프트를 재사용하는 예시",
                "짧은 범위에서 시작하고 단계별로 검증할 것",
            ),
        )
        log_event(con, "seed.input_created", "sample task input")
        con.commit()
    print("Seeded one sample request.")


if __name__ == "__main__":
    main()
