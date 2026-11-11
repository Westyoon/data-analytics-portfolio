# Data Analytics Portfolio

데이터를 수집하는 데서 끝내지 않고, **질문을 정의하고 → 품질을 검증하고 → 결과와 한계를 근거로 남긴 프로젝트**를 정리합니다.

[GitHub profile](https://github.com/Westyoon) · [5-minute guide](PORTFOLIO_GUIDE.md) · [Data QA checklist](playbook/data-quality-checklist.md)

## Featured case studies

### 01. Emergency Medical Capacity

`2026.07 - 2026.09` · `3-person team` · `Data pipeline / analysis / deployment`

식별자와 갱신주기가 다른 NEMC, HIRA, 주민등록 인구, 카카오 경로와 시군구 경계를 결합해 지역별 응급의료 취약도를 분석했습니다.

**What I worked on**

- 기관 1:1 매칭과 낮은 신뢰도 후보 분리
- `0`, 미수집, 미매칭과 오래된 관측을 구분하는 결측 정책
- 회귀·VIF·K-Means 분석과 데이터 계약
- 검증된 데이터 generation만 반영하는 원자적 배포

**Team troubleshooting preview**

- 기관명이 달라 JOIN되지 않음 → 다중 특성 기반 전역 1:1 매칭
- 일부 병상 API 실패 → 마지막 정상값과 원래 수집시각 유지
- 산출물 일부만 갱신될 위험 → staging 계약 검증 후 한 세대로 승격

[Case study](projects/emergency-medical-capacity/README.md) · [Source](https://github.com/Westyoon/embulance_score) · [Architecture](https://github.com/Westyoon/embulance_score/blob/main/ARCHITECTURE.md) · [Run locally](https://github.com/Westyoon/embulance_score#빠른-재현)

---

### 02. Adaptive Modality Selection

`2026.03 - 2026.05` · `3 contributors` · `Experiment implementation / validation` · `Private fork`

멀티모달 연합학습에서 client/modality selection이 모델 성능과 통신 비용에 미치는 영향을 비교했습니다.

**What I worked on**

- FedAvg/FedProx 기반 unimodal·multimodal 실험
- local training scope와 server-missing-modality ablation
- FLOPs, communication overhead와 round별 metric 분석
- W&B logging과 checkpoint 기반 장시간 실험 재개

**Troubleshooting preview**

- single-label과 multi-label 결과를 같은 loss로 비교할 수 없음 → 데이터셋별 criterion 분리
- 실험마다 metric step이 달라 비교가 어긋남 → round 기준 logging 정렬
- 중단된 장시간 실험 재현이 어려움 → server/client checkpoint 동시 저장

[Case study](projects/adaptive-modality-selection/README.md) · Source repository is private

---

### 03. JARVIS Gaze Tracking

`2026.07` · `3-person team` · `Gaze Tracking / field QA`

일반 RGB 웹캠에서 사용자별 시선 대상을 추정하고, 불확실한 관측에서는 기기를 선택하지 않도록 calibration과 진단 흐름을 개선했습니다.

**What I worked on**

- 사용자별 기기 영역 등록과 `UNKNOWN` rejection
- blink/recovery grace와 기기별 판정 영역
- 등록 영역과 현재 시선점을 분리해 보여주는 진단 UI
- 사용자 피드백을 거리·각도·시간 변수로 바꾸는 QA loop

**Troubleshooting preview**

- 깜빡임마다 dwell 초기화 → 제한된 recovery grace 적용
- 크기가 다른 기기에 같은 반경 사용 → device-specific `radius_scale`
- 얼굴 관측 손실 시 진단 화면까지 사라짐 → 등록 영역과 관측 시선점의 상태 분리

[Case study](projects/gaze-tracking-qa/README.md) · [Source](https://github.com/madcamp-official/26s-w3-c3-05) · [My commits](https://github.com/madcamp-official/26s-w3-c3-05/commits/main/?author=Westyoon)

## Supporting validation work

| Project | Period / team | My focus | Links |
|---|---|---|---|
| DByte SQL Data Service | 2025.05 - 2025.06 · 4-person team | tracking CRUD·ROLLUP, `MainGUI`, console flow | [Case study](projects/dbyte-sql-data-service/README.md) · [Source](https://github.com/Westyoon/DByte) |

## How to read this repository

각 case study는 다음 순서로 작성했습니다.

1. **Overview** - 무엇을 만들었고 왜 필요한가
2. **Project info** - 기간, 인원, 개인 역할과 stack
3. **Architecture** - 데이터와 기능이 흐르는 방식
4. **Troubleshooting** - 문제 → 원인 → 검토한 대안 → 적용 → 결과
5. **Evidence** - 원본 코드, 커밋, 분석 산출물과 테스트
6. **Run & limitations** - 실행 방법과 아직 해결하지 못한 범위

## Repository structure

```text
projects/                         project case studies
playbook/data-quality-checklist.md
tests/                            executable QA example tests
PORTFOLIO_GUIDE.md                five-minute review path
```

팀 프로젝트는 팀 전체 결과와 개인 담당 범위를 구분하며, 공개 저장소에서 확인되지 않는 수치는 새로 만들어 적지 않습니다.
