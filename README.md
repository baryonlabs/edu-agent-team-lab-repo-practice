# Agent Team Lab Repo

이 저장소는 교육 중 수강자가 자신의 업무 목표를 입력하고, 그 목표를 수행하는 범용 Agent Team을 단계적으로 조립하는 실습 repo입니다.
기본 코드 예제는 타로 상담 흐름을 사용하지만, 실습의 목적은 타로가 아니라 **사용자가 추가로 입력한 업무 목표를 이루는 에이전트**를 만드는 방법을 익히는 데 있습니다.

GitHub 공개 링크: https://github.com/baryonlabs/edu-agent-team-lab-repo-practice

## 시작하기

처음에는 repo를 내려받고, 프롬프트를 하나씩 실행하면서 커밋으로 진도를 남깁니다.

```bash
git clone https://github.com/baryonlabs/edu-agent-team-lab-repo-practice.git
cd edu-agent-team-lab-repo-practice
git log --oneline --reverse
```

프롬프트는 한 번에 1~6단계를 모두 시키지 말고, 아래처럼 단계별로 끊어서 실행합니다.

### 시작 프롬프트 0. repo 내려받기

```text
GitHub에서 실습 repo를 내려받아 시작해라.
repo 주소는 https://github.com/baryonlabs/edu-agent-team-lab-repo-practice 이다.
내려받은 뒤 repo 루트로 이동하고 git log --oneline --reverse로 단계 커밋을 확인해라.
아직 파일을 수정하지 말고 현재 구조만 설명해라.
```

### 시작 프롬프트 1. 문서 읽고 자기 목표를 정리하기

```text
README.md와 docs/STAGE_GUIDE.md를 읽어라.
이 실습이 어떤 흐름으로 진행되는지 6단계로 요약하고,
내가 만들 업무 목표를 1문장으로 정리해라.
기존 자료와 기존 프롬프트에서 재사용할 만한 부분도 함께 적어라.
아직 코드는 수정하지 마라.
```

### 시작 프롬프트 2. 1단계만 실행하기

```text
prompts/01-repo-skeleton.md만 읽고 실행해라.
완료 후 find . -maxdepth 2 -type d | sort로 확인하고,
문제가 없으면 git commit -m "step 1: create repo skeleton"으로 커밋해라.
다음 단계는 내가 지시할 때까지 진행하지 마라.
```

### 이후 반복 프롬프트

```text
prompts/0N-<step-name>.md만 읽고 실행해라.
docs/STAGE_GUIDE.md의 해당 단계 확인 명령을 실행해라.
문제가 없으면 README.md의 지정된 커밋 메시지로 commit해라.
다음 단계는 내가 지시할 때까지 진행하지 마라.
```

## LLM 튜터 프롬프트

아래 프롬프트는 LLM이 이 repo의 커밋 히스토리를 보고, **첫 커밋을 Step 1로 간주해 실습을 단계별로 가이드**하도록 만들 때 사용합니다. 코드를 대신 끝까지 만들어 달라는 프롬프트가 아니라, 수강자가 각 단계에서 무엇을 보고 실행해야 하는지 설명하게 하는 프롬프트입니다.

```text
너는 이 repo의 실습 튜터다.

목표:
- git log --oneline --reverse의 첫 번째 step 커밋을 Step 1로 간주한다.
- 커밋 순서대로 Step 1부터 Step 6까지 실습을 안내한다.
- 한 번에 모든 단계를 진행하지 않는다.
- 현재 단계의 코드, 프롬프트, 확인 명령, 커밋 메시지만 설명한다.

먼저 실행할 것:
1. README.md를 읽어 전체 실습 목표를 파악한다.
2. docs/STAGE_GUIDE.md를 읽어 단계별 코드 지도를 파악한다.
3. COMMIT_LOG.md와 git log --oneline --reverse를 비교해 단계별 커밋을 확인한다.
4. prompts/ 디렉터리의 파일 목록을 확인한다.

응답 형식:
1. 현재 단계 번호와 목표
2. 읽어야 할 파일
3. 수정하거나 실행할 파일
4. 수강자가 알아야 할 핵심 개념 3개
5. 확인 명령
6. 성공 기준
7. 커밋 메시지
8. 다음 단계로 넘어가기 전에 나에게 확인할 질문

진행 규칙:
- Step 1부터 시작한다.
- 내가 "다음 단계"라고 말하기 전에는 Step 2로 넘어가지 않는다.
- 코드 변경이 필요하면 먼저 변경 계획을 짧게 설명한다.
- 확인 명령이 실패하면 커밋하지 않고 원인을 설명한다.
- 커밋은 해당 단계의 지정 메시지로만 만든다.
- data/*.db, logs/*.jsonl, .env, __pycache__는 커밋하지 않는다.

이제 Step 1을 시작해라.
```

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
| 2 | 사용자 업무 목표와 컨텍스트 정리 | `prompts/02-context-pack.md` | `step 2: add business context pack` |
| 3 | 반복 업무 절차 Skill 작성 | `prompts/03-tarot-skill.md` | `step 3: add tarot response skill` |
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

처음부터 다시 검수하려면 생성된 SQLite 파일을 지우고 실행합니다.

```bash
rm -f data/agent_team_lab.db
python backend/seed_order.py
python agents/tarot_agent.py
python conductor/daily_briefing.py
```

## 코드 설명

슬라이드의 단계별 설명과 실제 코드는 [docs/STAGE_GUIDE.md](docs/STAGE_GUIDE.md)에 1:1로 정리되어 있습니다.

- 교재 PDF: [docs/curriculum/ai-native-agent-curriculum.pdf](docs/curriculum/ai-native-agent-curriculum.pdf)
- `prompts/`: 단계별로 Claude Code에 넣는 프롬프트
- `context/`와 `CLAUDE.md`: Agent가 참고하는 사업 기준
- `skills/tarot-response.md`: 반복 업무 절차의 예시 파일
- `backend/`: SQLite 스키마와 연결 함수
- `agents/tarot_agent.py`: 입력 목표를 초안으로 바꾸는 단일 Agent 예시
- `approval_queue/app.py`: 사람이 승인/반려하는 화면
- `conductor/daily_briefing.py`: 운영 상태 브리핑

## 검수 기준

- `CLAUDE.md`, `context/`, `skills/`, `agents/`, `backend/`, `approval_queue/`, `conductor/`가 모두 존재한다.
- 사용자 목표 1건이 초안으로 생성되고 승인 큐에 남는다.
- Conductor가 승인 대기 건수와 최근 실행 로그를 브리핑한다.
- 각 단계가 Git commit으로 분리되어 있다.
