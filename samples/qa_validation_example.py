"""작은 데이터프레임에도 적용할 수 있는 QA 검증 예시."""

from dataclasses import dataclass

import pandas as pd


@dataclass(frozen=True)
class QualityReport:
    row_count: int
    duplicate_keys: int
    missing_required: dict[str, int]
    invalid_rows: int


def validate_hospital_snapshot(frame: pd.DataFrame) -> QualityReport:
    """병원 스냅샷의 키·필수값·수치 범위를 점검한다.

    결측을 0으로 채우지 않고 검증 결과로 반환하여 호출자가
    배치 중단, 검토 요청, 이전 정상본 유지 중 하나를 선택하게 한다.
    """

    required = ["hospital_id", "region_code", "available_beds", "total_beds"]
    missing_columns = sorted(set(required) - set(frame.columns))
    if missing_columns:
        raise ValueError(f"missing columns: {missing_columns}")

    missing = {column: int(frame[column].isna().sum()) for column in required}
    duplicate_keys = int(frame.duplicated("hospital_id", keep=False).sum())
    numeric = frame[["available_beds", "total_beds"]]
    invalid_mask = (
        numeric.isna().any(axis=1)
        | frame["total_beds"].le(0)
        | frame["available_beds"].lt(0)
        | frame["available_beds"].gt(frame["total_beds"])
    )

    return QualityReport(
        row_count=len(frame),
        duplicate_keys=duplicate_keys,
        missing_required=missing,
        invalid_rows=int(invalid_mask.sum()),
    )


if __name__ == "__main__":
    sample = pd.DataFrame(
        [
            {"hospital_id": "A1", "region_code": "11", "available_beds": 3, "total_beds": 10},
            {"hospital_id": "A2", "region_code": "11", "available_beds": -1, "total_beds": 8},
        ]
    )
    print(validate_hospital_snapshot(sample))

