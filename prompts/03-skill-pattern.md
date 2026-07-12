# Step 3 Prompt: 반복 업무 절차 Skill 작성

반복 프롬프트를 재사용 가능한 Skill 문서로 고정해라. 이 Skill은 특정 예시 도메인에 묶이지 않고 사용자가 입력한 업무 목표를 수행하는 절차를 설명해야 한다.

## 작성 파일

- `skills/response-pattern.md`

## 포함할 내용

- 입력 형식
- 출력 형식
- 업무 목표 해석 원칙
- 금지 표현
- 좋은 예시 2개
- 피해야 할 예시 1개

## 완료 조건

- 같은 입력 목표를 넣으면 항상 `입력 요약 -> 작업 흐름 -> 실행 조언 -> 확인 질문` 순서로 나온다.

## 단계 종료 커밋

```bash
git add .
git commit -m "step 3: add response skill"
```
