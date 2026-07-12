# Step 4 Prompt: 단일 Agent 구현

사용자가 입력한 업무 목표와 컨텍스트를 읽고 실행 초안을 생성하는 첫 Agent를 구현해라.

## 작성 파일

- `backend/db.py`
- `backend/schema.sql`
- `backend/seed_order.py`
- `agents/tarot_agent.py`

## 완료 조건

- `python backend/seed_order.py`로 샘플 목표를 넣을 수 있다.
- `python agents/tarot_agent.py`로 승인 대기 초안이 생성된다.
- 실제 LLM 호출 전이라도 Skill 규칙을 흉내 내는 deterministic draft가 생성되어야 한다.

## 단계 종료 커밋

```bash
git add .
git commit -m "step 4: implement tarot draft agent"
```
