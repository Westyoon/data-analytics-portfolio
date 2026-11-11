# 추가 직무 관련 프로젝트

## 1. DByte — SQL·JDBC 기반 의료 데이터 서비스

[저장소](https://github.com/Westyoon/DByte)

### 담당 근거

Git 이력에서 `Westyoon` 계정으로 상담 기록, 기관 리뷰, 건강 추적과 메인 GUI 관련 구현 커밋을 확인할 수 있습니다.

### 데이터 업무와의 연결

의료 서비스의 사용자 요구사항을 역할별 데이터 조회로 변환했습니다.

- 환자는 자신의 상담 기록을 조회
- 의사는 소속 기관의 상담 기록을 조회·수정·삭제
- 기관과 사용자 단위로 리뷰 수와 평균 평점을 집계
- 환자의 알레르기 정보와 처방 내용을 대조
- 건강 추적 기록을 날짜 순서로 조회

사용한 SQL 요소:

- `SELECT`, `INSERT`, `UPDATE`, `DELETE`
- 환자·상담·기관 테이블 `JOIN`
- 서브쿼리
- `COUNT`, `AVG`, `GROUP BY`
- 역할별 `VIEW`
- JDBC `PreparedStatement` 파라미터 바인딩

### 직무 활용 포인트

유관부서가 “특정 사용자의 기록”, “기관별 평균”, “의사에게 허용된 데이터”를 요청했을 때 이를 필터·JOIN·집계 조건으로 바꾸는 기초 경험입니다. 다만 분석용 대용량 warehouse나 Public Cloud SQL 운영 경험으로 과장하지 않습니다.

## 2. 선택적 얼굴 익명화 — 모델 threshold 검증

[저장소](https://github.com/Ewha-face-anonymizer/model)

### 파이프라인

```text
이미지·영상
→ MTCNN 얼굴 감지
→ ArcFace 512차원 임베딩
→ 코사인 거리 계산
→ 기준 인물 여부 판정
→ 비대상 얼굴 익명화
```

### 산출물 검증

얼굴 매칭에서 threshold를 임의로 정하면 본인을 가리거나 타인을 노출할 수 있습니다. 이를 줄이기 위해 다음 검증을 수행했습니다.

- threshold 변화에 따른 precision과 recall 분석
- 동일 인물 사진군과 여러 인물이 섞인 그룹 시나리오 분리
- 인물별 최적 threshold 탐색
- 원거리 소형 얼굴, 부분 가림, 빠른 움직임을 포함한 평가 조건 구성
- 프레임 스킵, 리사이즈, tracking 적용 전후 성능 비교

### 직무 활용 포인트

모델 결과를 단순 시연으로 판단하지 않고, 오류 비용이 다른 precision과 recall을 비교해 운영 기준을 조정한 경험입니다. “모델링 산출물 검증 및 결과 고도화”에 직접 연결할 수 있습니다.

## 3. JARVIS — 시선 추적 calibration과 현장 QA

[저장소](https://github.com/madcamp-official/26s-w3-c3-05)

### 담당 범위

프로젝트 README와 Git 이력에서 `Westyoon`의 담당은 Gaze Tracking으로 명시되어 있습니다.

- 얼굴·홍채 추적
- 사용자별 기기 등록
- 시선 대상 추정
- 시선·제스처 신호 결합
- 모니터링과 진단 UI

### 데이터 기반 개선 사례

실사용 환경에서는 깜빡임 뒤 UNKNOWN 프레임, 작은 전구의 좁은 등록 영역, 큰 모니터의 과도한 판정 영역 때문에 인식이 불안정했습니다.

이를 다음과 같이 개선했습니다.

- blink hold, recovery hold, candidate grace 조정
- target match tolerance와 unknown angle 기준 조정
- calibration coverage가 특정 자세 때문에 영구 미완료되는 경우 총 유효 프레임 기반 우회 조건 추가
- 모든 기기에 하나의 반경을 적용하지 않고 작은 전구에 기기별 radius scale 적용
- 등록 영역과 현재 시선 좌표를 표시하는 진단 지도로 오판정 원인 확인
- 얼굴 추적이 끊겨도 등록 영역은 유지하되 시선점은 실제 관측이 있을 때만 표시

### 직무 활용 포인트

사용자 피드백을 단순 감상으로 처리하지 않고, 거리·각도·유효 프레임·시간 허용치라는 측정 가능한 변수로 바꿔 이슈를 분석하고 결과를 고도화한 사례입니다.

## 4. 보조 사례로만 활용할 프로젝트

### AI Change

[저장소](https://github.com/Westyoon/ai-change)

Cloudflare D1 migration, JSON runtime data 검증, contract/unit/smoke test가 풍부해 데이터 계약과 QA 역량을 보여줄 수 있습니다. 다만 본질은 웹·게임 플랫폼이므로 OB 지원 포트폴리오의 핵심 사례보다 “품질 자동화 경험”의 보조 근거로 적합합니다.

### MouseKeeper

[저장소](https://github.com/madcamp-official/26s-w2-c3-09)

서버·Worker·모바일·인증·realtime·배포를 담당했고, 잘못된 파일 변경을 막기 위한 승인·계약·journal 구조가 있습니다. 데이터 분석보다는 안전한 시스템 운영과 요구사항 정의 경험을 묻는 면접에서 활용하는 편이 적절합니다.

### 제외한 프로젝트

- `MLHW`: 현재 Git 이력에서 본인 기여 근거를 확인하기 어려워 제외
- `OSPGoHome`: 확인된 본인 커밋이 주로 CSS·화면 구현이어서 데이터 직무 포트폴리오에서는 제외
- `NoteSnatcher`: 현재 기본 브랜치에서 본인 기여 근거가 명확하지 않아 제외
- 축제 웹사이트·파티 게임: 협업과 제품 구현 역량은 보여주지만 Data Analytics & Engineering 직무의 핵심 증거로는 우선순위가 낮음
