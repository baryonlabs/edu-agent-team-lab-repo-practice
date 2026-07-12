# Step 3 Prompt: 타로 답변 Skill 작성

반복 프롬프트를 재사용 가능한 Skill 문서로 고정해라.

## 작성 파일

- `skills/tarot-response.md`

## 포함할 내용

- 입력 형식
- 출력 형식
- 카드 해석 원칙
- 금지 표현
- 좋은 예시 2개
- 피해야 할 예시 1개

## 완료 조건

- 같은 주문을 넣으면 항상 `카드 해석 -> 종합 -> 조언 -> 확인 질문` 순서로 나온다.

## 단계 종료 커밋

```bash
git add .
git commit -m "step 3: add tarot response skill"
```

