# Step 6 Prompt: Conductor와 로깅 추가

Agent Team 운영 상태를 한 장 브리핑으로 요약하는 Conductor를 만들어라.

## 작성 파일

- `conductor/daily_briefing.py`
- `logs/.gitkeep`
- 필요하면 실행 로그 함수 추가

## 완료 조건

- 승인 대기, 승인, 반려 건수를 출력한다.
- 최근 draft 생성 내역을 보여준다.
- 나중에 Langfuse로 바꿀 수 있도록 로그 경로와 함수 이름을 분리한다.

## 단계 종료 커밋

```bash
git add .
git commit -m "step 6: add conductor briefing loop"
```
