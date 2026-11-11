# Data Analytics & Engineering Portfolio

> OB맥주 Bees T&A Student Intern 지원을 위해 데이터 전처리, QA, 모델 산출물 검증 경험을 중심으로 정리한 포트폴리오입니다.

## Profile

저는 데이터를 단순히 분석하는 데서 끝내지 않고, **원천 수집 → 정제·결합 → 품질 검증 → 모델링 → 서비스 제공**까지 연결하는 과정에 관심이 있습니다. 특히 서로 다른 기준으로 생성된 데이터를 결합할 때 발생하는 식별자 불일치, 결측, 이상값, 갱신 시점 차이를 명시적인 품질 규칙으로 관리해 왔습니다.

## Role Fit

| Bees T&A 직무 | 관련 경험 | 증거 |
|---|---|---|
| 데이터 전처리 및 QA | 공공 API 5종 결합, 스키마·범위·결측·신선도 검증 | [응급의료 데이터 파이프라인](docs/01-emergency-data-pipeline.md) |
| SQL/Python 기반 데이터 처리 | Python·pandas 기반 수집, 정규화, 집계, 파생지표 생성 | [소스 저장소](https://github.com/Westyoon/embulance_score/tree/main/scripts) |
| 모델 산출물 검증 | 회귀 R²·MAE, VIF, K-Means k 평가 및 결과 버전 일관성 점검 | [분석 검증 사례](docs/02-model-output-validation.md) |
| 데이터 이슈 도출·개선 | HIRA/NEMC 식별자 불일치, 중복 매칭, 오래된 병상값과 API 부분 실패 처리 | [QA 체크리스트](docs/03-data-qa-checklist.md) |
| 분석 결과 고도화 | 결측을 0으로 대체하지 않고 원인코드·후속조치·품질상태로 관리 | [결측 관리 사례](docs/01-emergency-data-pipeline.md#4-qa와-문제-해결) |
| 모델링 실험 지원 | 멀티모달 연합학습 실험, ablation, metric·checkpoint·W&B 기반 비교 | [연구 실험 검증](docs/02-model-output-validation.md#case-b-멀티모달-연합학습-실험) |
| SQL 기반 추출·제공 | JDBC PreparedStatement, VIEW, JOIN, GROUP BY 기반 의료 기록·리뷰 조회 | [SQL 데이터 활용](docs/05-additional-relevant-projects.md#1-dbyte--sql·jdbc-기반-의료-데이터-서비스) |
| 모델 결과 고도화 | 얼굴 매칭 Precision–Recall, threshold tuning과 시선 calibration 개선 | [추가 모델 검증 사례](docs/05-additional-relevant-projects.md) |

## Selected Projects

### 1. Emergency Medical Capacity Dashboard — Data Pipeline & QA

[원본 저장소](https://github.com/Westyoon/embulance_score) · [운영 대시보드](https://emergency-dashboard-production-e303.up.railway.app)

서로 다른 기관 식별자와 갱신주기를 가진 NEMC, HIRA, 행정안전부/KOSIS, 카카오 데이터를 결합해 지역별 응급의료 위험도를 산출하고 지도에서 제공하는 프로젝트입니다.

핵심 기여:

- NEMC `hpid`를 기준 모집단으로 고정하고 HIRA 의료인력을 LEFT JOIN하여 미매칭 기관이 사라지는 문제 방지
- 병원명·주소·전화·좌표·시설종별을 이용한 NEMC↔HIRA 전역 1:1 매칭 및 저신뢰 후보 분리
- 유효하지 않은 병상 수, API 부분 실패, 오래된 관측값을 0으로 덮지 않고 품질 상태와 감사 로그로 관리
- staging 검증을 통과한 데이터 generation만 운영으로 원자적 승격하고 실패 시 마지막 정상본 유지
- 원천값 기반 선형회귀, 다중공선성 점검, K-Means 군집화와 결과 파일 생성
- Python·Node 회귀 테스트 및 Docker/CI smoke test 구성

### 2. Adaptive Modality Selection — Model Experiment Validation

[원본 저장소 — 비공개](https://github.com/Westyoon/Adaptive-Modality-Selection)

멀티모달 연합학습 환경에서 클라이언트·모달리티 선택 전략을 비교하고, 데이터셋과 실험 조건별 모델 성능 및 통신 효율을 분석한 연구 구현 프로젝트입니다.

핵심 경험:

- 이미지·텍스트·멀티모달 데이터셋의 loader와 평가 흐름 관리
- FedAvg, FedProx, FedCola, BMSFed 등 조건별 실험 스크립트 구성
- `All`, `d_client`, `d_pair`, `m_pair` 학습 범위에 대한 ablation 비교
- accuracy, macro-F1, loss, 통신량, 모달리티 선택 비율 추적
- checkpoint 재개와 W&B metric logging으로 장시간 실험의 재현성과 비교 가능성 확보
- modality missing 상황과 데이터셋별 loss 차이를 반영한 결과 검증

### 3. DByte — SQL Data Extraction

[원본 저장소](https://github.com/Westyoon/DByte)

의료기관, 환자, 상담 기록, 건강 추적, 리뷰 데이터를 관계형 데이터베이스에서 조회·관리하는 Java/JDBC 프로젝트입니다. 직접 작성한 커밋에는 상담 기록, 기관 리뷰, 건강 추적과 메인 GUI 구현이 포함됩니다.

- `PreparedStatement`를 이용한 조건별 데이터 조회와 CRUD
- 환자·상담·의료기관 테이블 JOIN
- `COUNT`, `AVG`, `GROUP BY` 기반 기관·사용자별 리뷰 통계
- Patient/Doctor VIEW를 이용한 역할별 데이터 제공
- 처방 전 환자 알레르기 데이터 대조

### 4. Face Anonymizer — Threshold & Precision–Recall Validation

[원본 저장소](https://github.com/Ewha-face-anonymizer/model)

등록된 얼굴만 유지하고 나머지 얼굴을 익명화하는 모델 파이프라인에서 얼굴 매칭 threshold를 데이터로 조정했습니다.

- MTCNN 감지 → ArcFace 512차원 임베딩 → 코사인 거리 매칭 → OpenCV 익명화
- threshold별 Precision–Recall 분석
- 동일 인물·그룹 시나리오를 분리한 임계값 탐색
- 프레임 스킵·리사이즈·트래킹 적용 전후 A/B 비교
- 원거리 소형 얼굴, 가림, 빠른 움직임을 포함한 실패 조건 점검

### 5. JARVIS Gaze Tracking — Calibration & Field QA

[원본 저장소](https://github.com/madcamp-official/26s-w3-c3-05)

일반 웹캠의 시선과 제스처로 기기를 제어하는 프로젝트에서 Gaze Tracking을 담당했습니다.

- 사용자별 기기 등록과 시선 대상 추정
- calibration 유효 프레임과 coverage 조건 관리
- blink/recovery grace와 각도·거리 tolerance 조정
- 실제 사용 로그와 시연 피드백을 근거로 기기별 판정 영역 고도화
- 등록 영역·현재 시선점 진단 지도를 추가해 오판정 원인을 시각적으로 확인

세 프로젝트의 직무 연결과 근거는 [추가 관련 프로젝트](docs/05-additional-relevant-projects.md)에 정리했습니다.

## Data Quality Principles

1. **결측과 0을 구분합니다.** 측정값 0과 수집·매칭 실패는 분석 의미가 다릅니다.
2. **기준 모집단을 보존합니다.** 보강 데이터의 결측 때문에 원본 개체가 사라지지 않도록 결합 방식을 선택합니다.
3. **자동화된 판단에는 근거를 남깁니다.** 매칭점수, 후보, 원천 URL, 확인일과 예외 사유를 보존합니다.
4. **산출물의 세대를 섞지 않습니다.** 입력과 파생 결과의 버전을 함께 검증하고 한 묶음으로 배포합니다.
5. **실패를 숨기지 않습니다.** 일부 파일만 갱신하지 않고 이전 정상본을 유지하며 실패 원인을 노출합니다.

## Repository Guide

```text
.
├─ README.md
├─ docs/
│  ├─ 01-emergency-data-pipeline.md
│  ├─ 02-model-output-validation.md
│  ├─ 03-data-qa-checklist.md
│  └─ 04-interview-talking-points.md
│  └─ 05-additional-relevant-projects.md
├─ samples/
│  └─ qa_validation_example.py
└─ .gitignore
```

## Tech Stack

`Python` · `pandas` · `scikit-learn` · `SQL` · `JDBC` · `MySQL` · `REST API` · `Next.js` · `Node.js` · `Docker` · `GitHub Actions` · `Railway` · `W&B` · `PyTorch`

SQL/JDBC 프로젝트에서 JOIN, VIEW, 조건별 조회, 집계와 CRUD를 구현했습니다. 대규모 분석 쿼리와 window function은 추가로 보완하고 있으며, 본 포트폴리오의 중심은 실제로 수행한 Python 기반 ETL과 QA 경험입니다.

## Source & Scope

- 이 저장소는 기존 프로젝트의 전체 코드를 복제하지 않고, 지원 직무와 관련된 문제 해결 과정과 검증 근거를 요약합니다.
- 원천 데이터와 API 키는 포함하지 않습니다.
- 응급의료 위험도는 상대적 분석 지표이며 의료적 진단이나 실제 이송 지시를 위한 모델이 아닙니다.
- 연구 프로젝트는 기존 공개 연구 코드 기반의 확장·실험 구현이며 원 논문의 저작권과 출처를 존중합니다.

