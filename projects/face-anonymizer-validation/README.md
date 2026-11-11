# Selective Face Anonymization — Threshold Validation

> 등록된 얼굴은 유지하고 나머지 얼굴을 익명화하는 팀 프로젝트에서, 얼굴 매칭 threshold를 데이터로 검토하고 실패 조건을 분리했습니다.

[Team repository](https://github.com/Ewha-face-anonymizer/model) · [Contribution history](https://github.com/Ewha-face-anonymizer/model/commits/main/?author=Westyoon)

## Executive summary

| Item | Detail |
|---|---|
| Question | 어떤 cosine-distance threshold가 대상 인물 보존과 타인 익명화 사이의 오류를 줄일까? |
| Pipeline | MTCNN detection → ArcFace embedding → cosine distance → OpenCV anonymization |
| Validation | precision–recall, 인물별 threshold, 동일 인물·그룹 시나리오, A/B 처리 비교 |
| Failure cases | 원거리 소형 얼굴, 가림, 빠른 움직임, 프레임 스킵 |
| Tools | Python, PyTorch, ONNX Runtime, OpenCV |

## Why threshold selection mattered

얼굴 매칭 오류는 방향에 따라 비용이 다릅니다.

- threshold가 너무 엄격하면 등록한 얼굴까지 익명화됩니다.
- threshold가 너무 느슨하면 등록하지 않은 얼굴이 노출됩니다.

따라서 단일 데모에서 잘 보이는 값을 고르지 않고, threshold 변화에 따른 precision과 recall을 함께 비교했습니다.

## Validation design

```text
참조 얼굴 등록
→ 평가 이미지·영상에서 얼굴 감지
→ ArcFace 512차원 임베딩
→ cosine distance 계산
→ threshold별 TP / FP / FN 집계
→ precision–recall 비교
→ 실패 조건별 재검토
```

검증 조건을 다음과 같이 나눴습니다.

1. 같은 인물의 각도·표정·조명 변화
2. 여러 인물이 함께 등장하는 그룹 장면
3. 원거리의 작은 얼굴과 부분 가림
4. 빠른 움직임이 있는 영상
5. 프레임 스킵·리사이즈·tracking 적용 전후

## Interpretation

전체 평균 하나만 최적화하면 얼굴 크기나 인물에 따라 실패가 가려질 수 있습니다. 그래서 인물별 결과와 그룹 장면을 분리하고, 익명화 실패인 false positive를 특히 주의해 threshold를 검토했습니다.

운영 기준을 정할 때는 정확도만이 아니라 다음을 함께 봐야 합니다.

- 대상 인물 보존율
- 타인 노출 위험
- 처리 속도와 프레임 누락
- 얼굴 크기·가림별 성능 차이
- threshold가 바뀐 모델·임베딩 버전

## Evidence

- 전체 파이프라인과 실행법: [project README](https://github.com/Ewha-face-anonymizer/model#readme)
- threshold·precision–recall 검증 설명: [실험 및 검증](https://github.com/Ewha-face-anonymizer/model#실험-및-검증)
- 감지·임베딩·매칭·익명화 모듈: [`components/`](https://github.com/Ewha-face-anonymizer/model/tree/main/components)
- 테스트: [`tests/`](https://github.com/Ewha-face-anonymizer/model/tree/main/tests)

## Limitations

- 공개 README에는 평가 샘플 수와 최종 threshold별 수치표가 포함되어 있지 않아 이 문서에서 수치를 새로 주장하지 않습니다.
- 얼굴 데이터는 개인정보이므로 원본 평가 이미지를 포트폴리오에 복제하지 않습니다.
- 특정 카메라·거리·연령대에서 정한 threshold는 다른 환경으로 그대로 일반화되지 않을 수 있습니다.

[← Portfolio home](../../README.md)
