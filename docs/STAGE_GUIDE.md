# Stage Guide

이 문서는 슬라이드의 실습 단계와 실제 코드가 1:1로 맞도록 정리한 운영 가이드입니다.
기본 예제는 타로 상담 흐름이지만, 실제 실습의 목표는 사용자가 추가로 입력한 업무 목표를 수행하는 범용 에이전트를 조립하는 방법을 익히는 것입니다.

GitHub 공개 링크: https://github.com/baryonlabs/edu-agent-team-lab-repo-practice

## 시작 프롬프트

### 0. repo 내려받기

```text
GitHub에서 실습 repo를 내려받아 시작해라.
repo 주소는 https://github.com/baryonlabs/edu-agent-team-lab-repo-practice 이다.
내려받은 뒤 repo 루트로 이동하고 git log --oneline --reverse로 단계 커밋을 확인해라.
아직 파일을 수정하지 말고 현재 구조만 설명해라.
```

### 1. 문서 읽기

```text
README.md와 docs/STAGE_GUIDE.md를 읽어라.
이 실습이 어떤 흐름으로 진행되는지 6단계로 요약하고,
각 단계에서 어떤 파일을 수정하거나 확인하는지 표로 정리해라.
아직 코드는 수정하지 마라.
```

### 2. 한 단계씩 실행하기

```text
prompts/01-repo-skeleton.md만 읽고 실행해라.
완료 후 find . -maxdepth 2 -type d | sort로 확인하고,
문제가 없으면 git commit -m "step 1: create repo skeleton"으로 커밋해라.
다음 단계는 내가 지시할 때까지 진행하지 마라.
```

다음 단계부터는 `01`을 `02`~`06`으로 바꾸고, 각 단계의 확인 명령과 커밋 메시지를 이 문서의 단계별 설명에 맞춘다.

```text
prompts/0N-<step-name>.md만 읽고 실행해라.
docs/STAGE_GUIDE.md의 해당 단계 확인 명령을 실행해라.
문제가 없으면 README.md의 지정된 커밋 메시지로 commit해라.
다음 단계는 내가 지시할 때까지 진행하지 마라.
```

## 전체 코드 지도

| 영역 | 파일 | 역할 |
|---|---|---|
| 프롬프트 | `prompts/*.md` | 각 단계에서 Claude Code에 넣을 작업 지시 |
| 컨텍스트 | `CLAUDE.md`, `context/*.md` | Agent가 따라야 할 사업 기준과 문체 |
| Skill | `skills/tarot-response.md` | 반복 업무 절차를 문서화한 예시 파일 |
| Agent | `agents/tarot_agent.py` | 입력 목표를 읽고 초안을 생성하는 예시 Agent |
| Backend | `backend/db.py`, `backend/schema.sql` | SQLite 연결, 테이블, 실행 로그 |
| Approval Queue | `approval_queue/app.py` | 초안을 승인, 반려하는 Streamlit UI |
| Conductor | `conductor/daily_briefing.py` | 운영 상태와 최근 로그를 브리핑 |

## 단계별 설명

### Step 1. 저장소 골격

- 프롬프트: `prompts/01-repo-skeleton.md`
- 산출물: `agents/`, `context/`, `skills/`, `backend/`, `approval_queue/`, `conductor/`
- 알아야 할 것: 폴더는 기능 경계입니다. 나중에 Agent가 늘어나도 역할별 위치가 흔들리지 않아야 합니다.
- 확인 명령: `find . -maxdepth 2 -type d | sort`

### Step 2. 컨텍스트 팩

- 프롬프트: `prompts/02-context-pack.md`
- 산출물: `CLAUDE.md`, `context/business-overview.md`, `context/tone-examples.md`
- 알아야 할 것: 파인튜닝 전에 먼저 사용자 업무 목표와 기존 자료를 Markdown으로 고정합니다.
- 확인 명령: `sed -n '1,120p' CLAUDE.md`

### Step 3. 반복 업무 절차 Skill

- 프롬프트: `prompts/03-tarot-skill.md`
- 산출물: `skills/tarot-response.md`
- 알아야 할 것: Skill은 반복 프롬프트가 아니라 재사용 가능한 업무 절차입니다. 현재 파일명은 예제 유산이고, 내용은 사용자 목표에 맞게 바꿔 읽습니다.
- 확인 명령: `sed -n '1,160p' skills/tarot-response.md`

### Step 4. 단일 Agent

- 프롬프트: `prompts/04-single-agent.md`
- 산출물: `backend/db.py`, `backend/schema.sql`, `backend/seed_order.py`, `agents/tarot_agent.py`
- 알아야 할 것: Agent는 입력 목표를 읽고, Skill 규칙을 적용하고, 결과를 DB에 남깁니다.
- 확인 명령:

```bash
python backend/seed_order.py
python agents/tarot_agent.py
```

### Step 5. 승인 큐

- 프롬프트: `prompts/05-approval-queue.md`
- 산출물: `approval_queue/app.py`
- 알아야 할 것: 외부 발신 전에는 사람이 확인하는 큐가 있어야 합니다.
- 확인 명령:

```bash
streamlit run approval_queue/app.py
```

### Step 6. Conductor와 로깅

- 프롬프트: `prompts/06-conductor-logging.md`
- 산출물: `conductor/daily_briefing.py`, `run_logs` 테이블
- 알아야 할 것: Conductor는 개별 Agent를 직접 대체하지 않고 상태를 모아 운영 판단을 돕습니다.
- 확인 명령:

```bash
python conductor/daily_briefing.py
```

## 전체 검수

```bash
rm -f data/agent_team_lab.db
python backend/seed_order.py
python agents/tarot_agent.py
python conductor/daily_briefing.py
git log --oneline --reverse
```

성공 기준은 사용자 목표에 대한 draft 1건과 최근 실행 로그가 브리핑에 표시되는 것입니다.
