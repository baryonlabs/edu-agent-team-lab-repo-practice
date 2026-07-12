# Step 2 Prompt: 컨텍스트 팩 작성

사용자가 추가로 입력한 업무 목표를 Agent가 계속 참조할 수 있도록 Markdown 컨텍스트로 정리해라.

## 작성 파일

- `CLAUDE.md`: 작업 정체성, 금지사항, 답변 톤
- `context/business-overview.md`: 업무 목표, 대상 사용자, 운영 원칙
- `context/tone-examples.md`: 좋은 문체 예시와 피해야 할 문체

## 완료 조건

- Agent가 읽어도 바로 사용자 목표 기반 초안을 만들 수 있을 만큼 구체적이어야 한다.
- 개인정보, API Key, 실제 고객 실명은 넣지 않는다.

## 단계 종료 커밋

```bash
git add .
git commit -m "step 2: add business context pack"
```
