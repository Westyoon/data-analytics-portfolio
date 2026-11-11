# DByte — SQL/JDBC Data Service

> 의료 서비스의 역할별 요구를 관계형 데이터 조회·집계 조건으로 바꾼 학업용 Java/JDBC 프로젝트입니다.

[Source repository](https://github.com/Westyoon/DByte) · [Contribution history](https://github.com/Westyoon/DByte/commits/main/?author=Westyoon)

## Executive summary

| Item | Detail |
|---|---|
| Question | 환자·의사·기관별로 허용된 기록과 통계를 어떻게 조회·수정할까? |
| Contribution | 상담 기록, 기관 리뷰, 건강 추적과 메인 GUI 관련 구현 |
| SQL | SELECT/INSERT/UPDATE/DELETE, JOIN, subquery, VIEW, CTE, window function, GROUP BY |
| Access layer | JDBC `PreparedStatement`, 역할별 조건 분기 |
| Scope | 학업용 로컬 MySQL 프로토타입; 분석 warehouse나 운영 서비스로 표현하지 않음 |

## Requirements translated into queries

| User need | Query design |
|---|---|
| 환자가 자신의 상담 기록 확인 | `PatientView`에서 `userId` 조건 조회 |
| 의사가 소속 기관의 기록 관리 | `Medical`에서 기관을 확인한 뒤 `DoctorView` 조회 |
| 기관별 리뷰 품질 비교 | `AVG(rating)` window function과 `RANK()` |
| 기관·사용자별 리뷰 통계 | `COUNT`, `AVG`, `GROUP BY`, `HAVING` |
| 처방 전 알레르기 확인 | 환자 ID로 알레르기 조회 후 처방 문자열 대조 |
| 건강 기록 시간순 확인 | 사용자·기관 권한 확인 후 날짜 정렬 |

## Example query pattern

기관 평균 평점과 순위를 한 번에 제공하기 위해 CTE와 window function을 사용했습니다.

```sql
WITH review_with_avg AS (
    SELECT
        review_id,
        institution_id,
        rating,
        AVG(rating) OVER (PARTITION BY institution_id) AS institution_avg
    FROM Reviews
)
SELECT
    review_id,
    institution_id,
    rating,
    institution_avg,
    RANK() OVER (ORDER BY institution_avg DESC) AS institution_rank
FROM review_with_avg;
```

입력값은 문자열 연결 대신 `PreparedStatement` 파라미터로 바인딩했습니다.

## Evidence map

| Capability | Source |
|---|---|
| 역할별 상담 기록, VIEW, 처방·알레르기 확인 | [`AppointmentRecordsql.java`](https://github.com/Westyoon/DByte/blob/main/source/AppointmentRecordsql.java) |
| 리뷰 CRUD, CTE·window function, 집계 | [`InstitutionReview.java`](https://github.com/Westyoon/DByte/blob/main/source/InstitutionReview.java) |
| 건강 추적 기록 | [`Tracking.java`](https://github.com/Westyoon/DByte/blob/main/source/Tracking.java) |
| 화면 통합 | [`MainGUI.java`](https://github.com/Westyoon/DByte/blob/main/source/MainGUI.java) |

## Limitations and next steps

- 저장소에 완전한 DB schema, migration과 seed가 없어 처음부터 재현 가능한 패키지는 아닙니다.
- 연결 정보가 코드에 있는 학업용 구조입니다. 운영 환경이라면 환경변수·secret manager와 connection pool로 분리해야 합니다.
- 메서드가 UI와 데이터 접근을 함께 담당합니다. repository/service 계층 분리가 필요합니다.
- 권한 검사는 애플리케이션 분기뿐 아니라 DB 권한과 테스트로 보강해야 합니다.
- 대규모 분석 쿼리의 실행계획, index와 성능 검증은 범위에 포함되지 않았습니다.

이 케이스는 완성된 운영 시스템보다 **사용자 요구를 키·필터·JOIN·집계로 번역한 SQL 기초 경험**의 근거로 사용합니다.

[← Portfolio home](../../README.md)
