# Selective Face Anonymization — Contribution Note

> 등록한 얼굴은 유지하고 나머지 얼굴을 익명화하는 팀 프로젝트입니다. 이 문서는 공개 커밋으로 확인되는 개인 기여 범위만 기록합니다.

[Team repository](https://github.com/Ewha-face-anonymizer/model) · [My public commits](https://github.com/Ewha-face-anonymizer/model/commits/main/?author=Westyoon)

## Project info

| Item | Detail |
|---|---|
| Period | 2025.11 - 2026.05 |
| Team | 3-person team |
| Team goal | MTCNN detection → ArcFace embedding → cosine-distance matching → selective anonymization |
| Verified contribution | 평가용 얼굴 데이터 정리·업로드, conda 환경 파일 추가 |
| Public evidence | `data/input/Dataset/person31` - `person50`, `environment.yml` |

## Team project context

팀 저장소는 얼굴 감지, 임베딩, cosine-distance matching과 익명화를 하나의 파이프라인으로 연결합니다. threshold별 precision–recall과 영상 처리 비교도 프로젝트 README에 설명되어 있습니다.

이 기능들은 **팀 프로젝트 전체 결과**이며, 공개 커밋 기록만으로는 제 개인 구현이라고 주장하지 않습니다.

## My contribution evidence

| Scope | Evidence | Boundary |
|---|---|---|
| 평가 데이터 구성 | [`data/input/Dataset/`](https://github.com/Ewha-face-anonymizer/model/tree/main/data/input/Dataset) | 공개 이력상 `person31` - `person50` 이미지 업로드 |
| 실행 환경 | [`environment.yml`](https://github.com/Ewha-face-anonymizer/model/blob/main/environment.yml) | conda package 환경 파일 추가 |
| Commit history | [Westyoon commits](https://github.com/Ewha-face-anonymizer/model/commits/main/?author=Westyoon) | 코드 소유권이 아니라 실제 공개 변경 범위 확인용 |

## Why this is not a featured case

포트폴리오의 대표 사례는 문제 정의, 구현, 검증과 결과를 개인 기여로 추적할 수 있어야 합니다. 이 프로젝트의 공개 이력에서는 threshold 분석 코드와 핵심 파이프라인이 제 커밋으로 확인되지 않으므로 대표 프로젝트와 profile README에서 제외했습니다.

## Privacy and limitations

- 얼굴 이미지는 개인정보와 라이선스 검토가 필요한 데이터이므로 이 포트폴리오에 복제하거나 미리보기로 삽입하지 않습니다.
- 원본 팀 저장소의 공개 이미지도 재사용 전에 촬영 동의와 이용 범위를 별도로 확인해야 합니다.
- 평가 표본 수, 최종 threshold와 성능 수치는 개인 기여 근거가 없어 이 문서에서 주장하지 않습니다.
- 개인 기여를 확장하려면 본인이 작성한 분석 notebook, 실험 로그나 PR 근거가 추가로 필요합니다.

[← Portfolio home](../../README.md)
