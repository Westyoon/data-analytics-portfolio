# Adaptive Modality Selection — Experiment Validation

> 멀티모달 연합학습에서 모든 업데이트를 동일하게 사용하지 않고, 클라이언트·모달리티 선택 전략이 성능과 통신 비용에 미치는 영향을 비교한 연구 구현 프로젝트입니다.

[Private source repository](https://github.com/Westyoon/Adaptive-Modality-Selection) · [FedCola paper](https://arxiv.org/abs/2404.12467)

## Executive summary

| Item | Detail |
|---|---|
| Question | 정보량과 보유 모달리티가 다른 클라이언트 중 어떤 업데이트를 학습·집계할까? |
| Contribution | 실험 스크립트, 선택 범위 ablation, missing-modality 평가, metric·checkpoint·W&B 기반 비교 |
| Comparison | FedAvg, FedProx, FedCola, BMSFed 등 |
| Datasets | CIFAR-100, AG News, UPMC Food-101, MM-IMDb 등 |
| Metrics | accuracy, macro-F1, loss, 통신량, 선택 비율 |
| Access | 연구 코드와 로그는 비공개이며, 공개 가능한 실험 구조와 검증 원칙만 이 문서에 정리 |

## Experiment question

멀티모달 연합학습에서는 클라이언트마다 가진 이미지·텍스트 정보량과 모달리티 구성이 다릅니다. 모든 로컬 업데이트를 같은 비용으로 학습·전송하는 기준선과, 유의미한 클라이언트·모달리티 쌍을 선택하는 전략을 같은 조건에서 비교했습니다.

핵심은 최고 수치 하나가 아니라 다음 질문에 답할 수 있게 실험을 구성하는 것이었습니다.

- 어떤 데이터셋과 알고리즘을 비교했는가?
- 클라이언트 전체와 개별 모달리티 중 어디까지 학습했는가?
- 이미지나 텍스트가 없을 때도 같은 경향이 유지되는가?
- 통신량 감소와 성능 변화가 같은 round·metric 정의로 계산되었는가?

## Experiment matrix

| Axis | Values |
|---|---|
| Algorithm | FedAvg, FedProx, FedCola, BMSFed 등 |
| Local training scope | `All`, `d_client`, `d_pair`, `m_pair` |
| Data type | image-only, text-only, image+text |
| Label type | single-label, multi-label |
| Stress condition | image missing, text missing, no modality missing |
| Evaluation | accuracy, macro-F1, loss, communication cost, selection ratio |

`All → d_client → d_pair → m_pair` 순서로 학습 범위를 좁혀, 선택의 단위가 성능과 계산량에 미치는 영향을 분리했습니다.

## Validation workflow

```mermaid
flowchart LR
    A[실험 설정 고정] --> B[데이터셋·loss 확인]
    B --> C[학습·W&B logging]
    C --> D[checkpoint 저장·재개]
    D --> E[round별 metric 정렬]
    E --> F[ablation·통신량 비교]
    F --> G[missing-modality 검증]
```

### Reliability controls

- MM-IMDb 같은 multi-label 데이터에는 `BCEWithLogitsLoss`, single-label 데이터에는 분류 loss를 구분했습니다.
- 조건별 shell script에 데이터셋, 알고리즘, 선택 범위와 seed를 명시해 수동 설정 차이를 줄였습니다.
- W&B의 round와 metric step을 연결해 서로 다른 실행을 같은 x축에서 비교했습니다.
- server/client checkpoint를 함께 저장해 장시간 실행 중단 후에도 같은 상태에서 재개했습니다.
- accuracy만 보지 않고 macro-F1과 모달리티별 head 결과를 함께 확인했습니다.
- 통신량은 선택된 다운로드·업로드 단위를 round별로 집계했습니다.

## Evidence available in the private repository

- 알고리즘·클라이언트·서버 구현: `src/algorithm/`, `src/client/`, `src/server/`
- 조건별 실행 스크립트: `scripts/fedavg/`, `scripts/fedprox/`, `scripts/bmsfed/`, `scripts/ours/`
- 학습 범위 ablation: `scripts/local_client_scope/`
- missing-modality 실험: `scripts/server_missing_modality/`
- 결과 분석: `analysis/main_table.ipynb`, `analysis/comm.ipynb`, `analysis/selection_ratio/`
- 통신량 요약: `analysis/communication_overehad/`

접근 권한이 없는 방문자는 위 경로를 열 수 없습니다. 그래서 이 케이스는 공개 저장소 프로젝트보다 보조 근거로 취급합니다.

## Attribution and limitations

- 기반 구현은 공개된 멀티모달 연합학습 연구 코드와 FedCola 연구를 확장한 것입니다. 기반 알고리즘을 개인의 독창적 발명으로 주장하지 않습니다.
- 대규모 실험은 GPU·데이터 준비와 긴 실행 시간이 필요해 이 포트폴리오 저장소만으로 즉시 재현할 수 없습니다.
- 일부 데이터셋 이름과 스크립트에는 기존 코드의 표기 불일치가 남아 있어 실행 전 설정 확인이 필요합니다.
- 최종 평가는 단일 최고 성능보다 동일 조건, 반복 실행, 통신 비용과 실패 조건을 함께 봐야 합니다.

## What this demonstrates

- 비교 가능한 실험 행렬 설계
- 데이터셋별 metric·loss 정의 검증
- ablation과 실패 조건 분석
- 장시간 모델 실험의 추적과 재개
- 성능과 시스템 비용을 함께 해석하는 방식

[← Portfolio home](../../README.md)
