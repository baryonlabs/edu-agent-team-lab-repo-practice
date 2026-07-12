# Step 5 Prompt: 승인 큐 구현

외부 발신물 또는 실행 전 초안을 바로 보내지 않고 승인 대기 상태로 모으는 UI와 상태 변경 로직을 만들어라.

## 작성 파일

- `approval_queue/app.py`
- 필요하면 `backend/db.py`를 확장한다.

## 완료 조건

- Streamlit에서 승인 대기 초안을 볼 수 있다.
- `approve`, `reject` 상태 변경이 DB에 저장된다.
- 수정 발송은 아직 구현하지 않아도 된다.

## 단계 종료 커밋

```bash
git add .
git commit -m "step 5: add approval queue backend"
```
