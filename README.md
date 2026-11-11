<div align="center">

# Data Analytics Portfolio

**From raw data to reliable decisions.**

서로 다른 원천의 데이터를 연결하고, 결측·식별자·버전 문제를 검증 가능한 규칙으로 바꾸며, 분석 결과를 재현 가능한 산출물로 만드는 과정을 기록합니다.

[Selected Work](#selected-work) · [Working Principles](#working-principles) · [Repository Guide](#repository-guide) · [5-minute Tour](PORTFOLIO_GUIDE.md)

[![Portfolio QA](https://github.com/Westyoon/data-analytics-portfolio/actions/workflows/quality.yml/badge.svg)](https://github.com/Westyoon/data-analytics-portfolio/actions/workflows/quality.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-2f4f4f.svg)](LICENSE)

</div>

## At a glance

| Focus | What I work on | Evidence in this repository |
|---|---|---|
| Data preparation | API 수집, 스키마 정규화, entity resolution, 결측 정책 | [응급의료 데이터 파이프라인](projects/emergency-medical-capacity/README.md) |
| Analysis & validation | 회귀 진단, 군집 비교, ablation, metric 일관성 | [모델 실험 검증](projects/adaptive-modality-selection/README.md) |
| Data access | 역할별 조회, JOIN, 집계, window function, JDBC | [SQL 데이터 서비스](projects/dbyte-sql-data-service/README.md) |
| Quality assurance | 데이터 계약, 실패 격리, threshold·calibration 검증 | [데이터 QA 체크리스트](playbook/data-quality-checklist.md) |

## Selected work

대표 프로젝트는 기술 이름이 아니라 **질문 → 판단 → 결과 → 근거** 순서로 정리했습니다.

| Project | Question | Headline evidence | Links |
|---|---|---|---|
| **Emergency Medical Capacity** | 식별자와 갱신주기가 다른 의료 데이터를 어떻게 안전하게 결합할까? | 5개 원천을 하나의 파이프라인으로 연결하고, 분석 스냅샷 196개 지역에서 진단 회귀 `R² 0.8614`, `MAE 3.0653` 기록 | [Case study](projects/emergency-medical-capacity/README.md) · [Source](https://github.com/Westyoon/embulance_score) · [Metrics](https://github.com/Westyoon/embulance_score/blob/main/data/regression_metrics.json) |
| **Adaptive Modality Selection** | 멀티모달 연합학습에서 어떤 클라이언트·모달리티 업데이트를 선택할까? | 알고리즘·학습 범위·결측 모달리티 조건을 실험 행렬로 고정하고 accuracy, macro-F1, loss, 통신량을 같은 기준으로 비교 | [Case study](projects/adaptive-modality-selection/README.md) |
| **DByte SQL Data Service** | 사용자 역할별 요구를 안전한 조회·집계 조건으로 어떻게 바꿀까? | `PreparedStatement`, 역할별 VIEW, JOIN, CTE·window function, `GROUP BY`를 이용한 의료 기록·리뷰 조회 | [Case study](projects/dbyte-sql-data-service/README.md) · [Source](https://github.com/Westyoon/DByte) |

> 회귀 수치는 위험도 산식의 민감도를 확인한 특정 데이터 스냅샷의 진단 결과입니다. 독립적인 예측 성능이나 인과 효과로 해석하지 않습니다.

### Featured case: emergency medical data

응급의료 프로젝트에서는 화면보다 데이터가 틀린 상태로 다음 단계에 넘어가지 않게 하는 데 집중했습니다.

- NEMC 기관을 기준 모집단으로 고정하고 HIRA 데이터를 LEFT JOIN해 미매칭 기관을 보존했습니다.
- 이름·주소·전화·좌표·기관종별을 함께 비교해 전역 1:1 기관 매칭을 수행했습니다.
- `0`, `NULL`, 미수집, 오래된 관측을 구분하고 원인코드와 후속조치를 남겼습니다.
- 수집·분석·화면 계약을 모두 통과한 데이터 세대만 원자적으로 승격했습니다.
- 회귀·VIF·K-Means 결과를 입력 데이터와 같은 세대로 관리했습니다.

[전체 케이스 스터디 보기 →](projects/emergency-medical-capacity/README.md)

## Additional work

| Project | Validation focus | Evidence |
|---|---|---|
| **Selective Face Anonymization** | 얼굴 매칭 threshold의 precision–recall trade-off와 실패 조건 | [Case study](projects/face-anonymizer-validation/README.md) · [Team repository](https://github.com/Ewha-face-anonymizer/model) |
| **JARVIS Gaze Tracking** | calibration coverage, blink/recovery grace, 기기별 판정 영역 | [Case study](projects/gaze-tracking-qa/README.md) · [Team repository](https://github.com/madcamp-official/26s-w3-c3-05) |

## Working principles

1. **결측과 0을 구분합니다.** 측정값 0과 수집·매칭 실패는 분석 의미가 다릅니다.
2. **기준 모집단을 보존합니다.** 보강 원천의 결측 때문에 원본 개체가 사라지지 않게 결합 방식을 선택합니다.
3. **자동화된 판단에 근거를 남깁니다.** 후보, 점수, 원천, 확인 시점과 예외 사유를 보존합니다.
4. **입력과 산출물의 세대를 맞춥니다.** 일부 파일만 갱신하지 않고 검증된 묶음으로 배포합니다.
5. **결과와 한계를 함께 적습니다.** 목표값, 실측값, 진단 지표와 예측 성능을 구분합니다.

## Repository guide

```text
.
├─ README.md                         # 포트폴리오 랜딩 페이지
├─ PORTFOLIO_GUIDE.md                # 5분 검토 동선
├─ projects/
│  ├─ emergency-medical-capacity/    # 데이터 파이프라인·분석·QA
│  ├─ adaptive-modality-selection/   # 모델 실험 설계·검증
│  ├─ dbyte-sql-data-service/        # SQL/JDBC 데이터 접근
│  ├─ face-anonymizer-validation/    # threshold 검증
│  └─ gaze-tracking-qa/              # calibration·현장 QA
├─ playbook/
│  └─ data-quality-checklist.md       # 재사용 가능한 검토 기준
├─ tests/                            # 포함된 QA 예시의 회귀 테스트
└─ .github/workflows/quality.yml     # 문법·테스트 자동 검증
```

각 케이스 스터디는 `Executive summary → Question → Approach → Evidence → Limitations` 순서를 따릅니다. 원본 저장소의 전체 코드를 복제하지 않고, 이 저장소에서는 판단 과정과 근거로 가는 길을 제공합니다.

## Run the included QA example

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# PowerShell: .\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python projects/emergency-medical-capacity/src/qa_validation_example.py
python -m pytest
```

이 예시는 병원 스냅샷의 필수 컬럼, 중복키, 결측과 병상 수치 범위를 검사합니다. 실제 응급의료 프로젝트의 전체 파이프라인은 [원본 저장소](https://github.com/Westyoon/embulance_score)에 있습니다.

## Toolkit

- **Analysis:** Python, pandas, scikit-learn, PyTorch, Jupyter
- **Data:** SQL, MySQL, JDBC, REST API, CSV/JSON data contracts
- **Delivery:** Next.js, Node.js, Docker, GitHub Actions, Railway, W&B
- **Validation:** pytest/unittest, regression tests, smoke tests, threshold analysis, experiment tracking

## Scope & attribution

- 팀 프로젝트는 개인 담당 범위와 팀 전체 결과를 구분해 작성했습니다.
- 비공개 연구 저장소는 코드 접근 제한을 명시하고 공개 가능한 실험 구조만 요약했습니다.
- 공개 연구 코드를 확장한 경우 원 논문과 기반 구현을 케이스 스터디에 표시했습니다.
- 원천 데이터, 개인정보와 API 키는 이 저장소에 포함하지 않습니다.

GitHub: [@Westyoon](https://github.com/Westyoon)
