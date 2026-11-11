# Data quality checklist

분석 요청을 데이터 추출부터 전달까지 진행할 때 사용하는 재사용 가능한 체크리스트입니다. 모든 항목을 기계적으로 통과시키기보다, 해당하지 않는 항목과 예외 사유도 함께 기록합니다.

## 1. Define the request

- [ ] 사용 목적과 최종 사용자를 확인했는가?
- [ ] 어떤 의사결정에 쓰이는지 한 문장으로 적었는가?
- [ ] 필요한 행 단위(grain)와 기준키를 정의했는가?
- [ ] 기간, 지역, 필터, 단위와 마감 시점을 확인했는가?
- [ ] `0`, `NULL`, 미수집, 미해당의 의미를 구분했는가?
- [ ] 개인정보·민감정보·외부 제공 제한을 확인했는가?

## 2. Extract and transform

- [ ] 원천, 추출 시각과 쿼리·스크립트 버전을 기록했는가?
- [ ] 중복키가 있는가? 있다면 허용되는 중복인가?
- [ ] JOIN 전후 행 수와 매칭률을 비교했는가?
- [ ] 기준 모집단이 보강 원천의 결측 때문에 사라지지 않는가?
- [ ] 문자열·날짜·코드·통화·단위를 표준화했는가?
- [ ] 파생변수의 분모 0과 이상 범위를 처리했는가?

## 3. Validate accuracy and completeness

- [ ] 필수 컬럼 결측 수와 결측률을 확인했는가?
- [ ] 범주값이 허용 목록 안에 있는가?
- [ ] 수치 최소·최대·분위수가 현실적인가?
- [ ] 합계와 세부 그룹 합계가 일치하는가?
- [ ] 이전 배치 대비 행 수·핵심 지표 변화가 설명 가능한가?
- [ ] 실패한 원천을 실제 값 `0`으로 대체하지 않았는가?
- [ ] 오래된 값은 원래 기준시각과 함께 표시되는가?

## 4. Validate analysis and model outputs

- [ ] 학습·검증 데이터의 기준 시점이 같은가?
- [ ] target leakage 또는 점수의 순환 정의가 없는가?
- [ ] 평가 모집단과 제외 조건이 문서화되었는가?
- [ ] baseline과 동일한 metric 정의로 비교했는가?
- [ ] 평균뿐 아니라 분포, 잔차와 실패 사례를 확인했는가?
- [ ] 목표값, 실측값과 진단 지표를 구분했는가?
- [ ] 입력 데이터 변경 시 종속 산출물을 함께 재생성했는가?

## 5. Publish and hand off

- [ ] 컬럼 정의, 단위와 예시를 함께 제공했는가?
- [ ] 필터 조건과 데이터 기준시각을 표시했는가?
- [ ] 품질 한계와 사용 금지 조건을 적었는가?
- [ ] 검증된 산출물 세대가 한 묶음으로 배포되는가?
- [ ] 재실행 방법, 실패 시 복구와 담당 후속조치를 정리했는가?
- [ ] 민감한 원천값, 개인정보와 secret이 결과물에 없는가?

## Minimal handoff record

```yaml
request:
  purpose: ""
  owner: ""
  delivered_at: ""
dataset:
  grain: ""
  primary_key: []
  filters: {}
  source_as_of: ""
quality:
  row_count: 0
  duplicate_key_rows: 0
  missing_required: {}
  known_limitations: []
reproducibility:
  code_version: ""
  command: ""
  output_generation: ""
```

실행 가능한 작은 예시는 [hospital snapshot validator](../projects/emergency-medical-capacity/src/qa_validation_example.py)에 있습니다.

[← Portfolio home](../README.md)
