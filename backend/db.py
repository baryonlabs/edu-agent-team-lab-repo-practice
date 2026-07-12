from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data" / "agent_team_lab.db"
SCHEMA_PATH = ROOT / "backend" / "schema.sql"


def connect() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(exist_ok=True)
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con


def init_db() -> None:
    with connect() as con:
        con.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))
        con.commit()


def log_event(con: sqlite3.Connection, event: str, detail: str) -> None:
    con.execute("insert into run_logs(event, detail) values (?, ?)", (event, detail))

