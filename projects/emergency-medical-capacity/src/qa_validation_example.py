"""Small, executable data-quality checks for a hospital snapshot."""

from __future__ import annotations

from dataclasses import asdict, dataclass

import pandas as pd


@dataclass(frozen=True)
class QualityReport:
    """Summary returned before a snapshot can be promoted downstream."""

    row_count: int
    duplicate_key_rows: int
    missing_required: dict[str, int]
    invalid_value_rows: int

    @property
    def passed(self) -> bool:
        return (
            self.duplicate_key_rows == 0
            and not any(self.missing_required.values())
            and self.invalid_value_rows == 0
        )

    def to_dict(self) -> dict[str, object]:
        return {**asdict(self), "passed": self.passed}


def validate_hospital_snapshot(frame: pd.DataFrame) -> QualityReport:
    """Validate keys, required values, and bed-count ranges.

    Missing or non-numeric values are reported instead of being replaced with
    zero. The caller can then stop the batch, request review, or keep the last
    known-good snapshot.
    """

    required = ["hospital_id", "region_code", "available_beds", "total_beds"]
    missing_columns = sorted(set(required) - set(frame.columns))
    if missing_columns:
        raise ValueError(f"missing columns: {missing_columns}")

    missing = {column: int(frame[column].isna().sum()) for column in required}
    duplicate_key_rows = int(frame.duplicated("hospital_id", keep=False).sum())

    available_beds = pd.to_numeric(frame["available_beds"], errors="coerce")
    total_beds = pd.to_numeric(frame["total_beds"], errors="coerce")
    invalid_mask = (
        frame[["hospital_id", "region_code"]].isna().any(axis=1)
        | available_beds.isna()
        | total_beds.isna()
        | total_beds.le(0)
        | available_beds.lt(0)
        | available_beds.gt(total_beds)
    )

    return QualityReport(
        row_count=len(frame),
        duplicate_key_rows=duplicate_key_rows,
        missing_required=missing,
        invalid_value_rows=int(invalid_mask.sum()),
    )


if __name__ == "__main__":
    sample = pd.DataFrame(
        [
            {
                "hospital_id": "A1",
                "region_code": "11",
                "available_beds": 3,
                "total_beds": 10,
            },
            {
                "hospital_id": "A2",
                "region_code": "11",
                "available_beds": -1,
                "total_beds": 8,
            },
        ]
    )
    print(validate_hospital_snapshot(sample).to_dict())
