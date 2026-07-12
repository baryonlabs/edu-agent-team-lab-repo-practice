# Step 1 Prompt: 저장소 골격 만들기

너는 이 실습 repo의 페어 프로그래머다. 빈 폴더를 Agent Team 실습용 저장소로 바꿔라.

## 만들어야 할 구조

- `CLAUDE.md`
- `context/`
- `skills/`
- `agents/`
- `backend/`
- `approval_queue/`
- `conductor/`
- `data/`
- `logs/`

## 완료 조건

- 각 폴더의 역할이 `README.md` 또는 `.gitkeep`으로 남아 있어야 한다.
- 실행 산출물(`data/*.db`, `logs/*.jsonl`)은 Git에 올라가지 않도록 `.gitignore`에 추가한다.

## 단계 종료 커밋

```bash
git add .
git commit -m "step 1: create repo skeleton"
```

