# Agent Team Lab Repo

이 저장소는 교육 중 수강자가 빈 폴더에서 Agent Team 운영 골격까지 직접 조립하는 실습 repo입니다.

## 학습 방식

각 단계는 `prompts/`의 프롬프트를 Claude Code에 붙여 넣어 완성합니다. 단계가 끝나면 반드시 테스트하고 커밋합니다.

```bash
git status
git add .
git commit -m "step N: ..."
```

## 단계 흐름

| 단계 | 목표 | 프롬프트 | 완료 커밋 |
|---|---|---|---|
| 1 | 저장소 골격 만들기 | `prompts/01-repo-skeleton.md` | `step 1: create repo skeleton` |
| 2 | 컨텍스트 팩 작성 | `prompts/02-context-pack.md` | `step 2: add business context pack` |
| 3 | 타로 답변 Skill 작성 | `prompts/03-tarot-skill.md` | `step 3: add tarot response skill` |
| 4 | 단일 Agent 구현 | `prompts/04-single-agent.md` | `step 4: implement tarot draft agent` |
| 5 | 승인 큐 구현 | `prompts/05-approval-queue.md` | `step 5: add approval queue backend` |
| 6 | Conductor와 브리핑 | `prompts/06-conductor-logging.md` | `step 6: add conductor briefing loop` |

## 실행

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python backend/seed_order.py
python agents/tarot_agent.py
python conductor/daily_briefing.py
streamlit run approval_queue/app.py
```

## 검수 기준

- `CLAUDE.md`, `context/`, `skills/`, `agents/`, `backend/`, `approval_queue/`, `conductor/`가 모두 존재한다.
- 타로 주문 1건이 초안으로 생성되고 승인 큐에 남는다.
- Conductor가 승인 대기 건수와 최근 실행 로그를 브리핑한다.
- 각 단계가 Git commit으로 분리되어 있다.

