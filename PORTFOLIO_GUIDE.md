# 5-minute portfolio tour

이 문서는 처음 방문한 사람이 포트폴리오의 핵심을 짧은 시간 안에 검토할 수 있도록 만든 탐색 가이드입니다.

## 0:00–0:30 — 전체 방향

[루트 README](README.md)의 `At a glance`와 `Selected work`를 먼저 확인합니다.

핵심 주제는 세 가지입니다.

1. 여러 데이터 원천을 같은 분석 단위로 연결하기
2. 결측·식별자·갱신 실패를 명시적인 품질 규칙으로 관리하기
3. 모델과 분석 결과를 같은 조건에서 비교하고 재현하기

## 0:30–2:30 — 대표 케이스

[Emergency Medical Capacity](projects/emergency-medical-capacity/README.md)를 읽습니다.

다음 판단을 중심으로 보면 됩니다.

- 왜 NEMC 기관을 기준 모집단으로 선택했는가?
- 왜 기관명을 단순 문자열 JOIN하지 않았는가?
- 왜 미매칭을 0명으로 채우지 않았는가?
- 왜 회귀 결과를 예측 성능이 아니라 산식 진단으로 해석하는가?
- 왜 staging 검증과 원자적 승격이 필요한가?

근거가 필요하면 케이스 스터디의 `Evidence map`에서 원본 코드, 데이터 산출물과 테스트로 이동합니다.

## 2:30–3:30 — 실험 검증

[Adaptive Modality Selection](projects/adaptive-modality-selection/README.md)에서 실험 조건을 비교 가능한 형태로 고정한 방식을 확인합니다.

- 알고리즘, 데이터셋, 학습 범위와 missing-modality 조건을 분리했는가?
- single-label과 multi-label 데이터의 loss를 구분했는가?
- 장시간 실험을 재개하고 같은 metric step으로 비교할 수 있는가?

이 프로젝트는 비공개 연구 저장소이므로 공개 가능한 구조와 검증 원칙만 제공합니다.

## 3:30–4:15 — SQL과 데이터 제공

[DByte SQL Data Service](projects/dbyte-sql-data-service/README.md)에서 사용자 요구를 조회 조건으로 바꾼 사례를 확인합니다.

- 환자와 의사에게 서로 다른 범위의 데이터를 제공하는 방식
- JOIN, VIEW, 집계와 window function을 사용한 방식
- 학업용 프로토타입의 한계를 명시한 방식

## 4:15–5:00 — 품질 기준과 보조 사례

- [데이터 QA 체크리스트](playbook/data-quality-checklist.md): 분석 전후에 반복해서 사용하는 검토 기준
- [QA 코드 예시](projects/emergency-medical-capacity/src/qa_validation_example.py): 작은 DataFrame에 적용한 실행 가능한 예시
- [Face Anonymizer](projects/face-anonymizer-validation/README.md): threshold의 오류 비용 비교
- [Gaze Tracking](projects/gaze-tracking-qa/README.md): 사용자 피드백을 calibration 변수로 바꾼 사례

## Evidence standard

이 포트폴리오의 수치와 주장은 가능한 한 다음 중 하나로 연결합니다.

- 공개 원본 코드나 커밋
- 분석 산출물 또는 명시된 데이터 스냅샷
- 테스트와 자동 검증
- 역할이 명시된 팀 문서

공개할 수 없는 코드, 목표값, 미완료 작업은 실제 결과처럼 표현하지 않습니다.
