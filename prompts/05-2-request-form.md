# Step 5-2 Prompt: 추가 요청 폼 만들기

승인 큐 화면에 사용자의 추가 요청을 입력받는 폼을 추가해라. 이 폼은 사용자가 자신의 업무 목표를 더 구체적으로 전달하는 통로다.

## 작성 파일

- `approval_queue/app.py`
- 필요하면 `backend/db.py`와 `backend/schema.sql`을 확장한다.

## 저장할 항목

- 요청 제목
- 업무 목표
- 기존 자료
- 제약 조건

## 완료 조건

- Streamlit에서 요청 폼을 볼 수 있다.
- 제출한 요청이 DB에 저장된다.
- 저장된 요청 목록을 다시 확인할 수 있다.
- 저장 시 실행 로그가 남는다.

## 프롬프트 예시

```text
승인 큐 화면에 사용자가 추가 요청을 남길 수 있는 폼을 추가해라.
필드: title, goal, context, constraints.
제출하면 intake_requests 테이블에 저장하고, 저장된 요청 목록을 화면 아래에 보여줘라.
입력값이 비어 있으면 저장하지 말고 에러를 표시해라.
```

## 단계 종료 커밋

```bash
git add .
git commit -m "step 5-2: add request intake form"
```

