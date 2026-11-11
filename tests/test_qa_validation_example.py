from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys

import pandas as pd
import pytest


MODULE_PATH = (
    Path(__file__).parents[1]
    / "projects"
    / "emergency-medical-capacity"
    / "src"
    / "qa_validation_example.py"
)
SPEC = spec_from_file_location("qa_validation_example", MODULE_PATH)
assert SPEC and SPEC.loader
qa = module_from_spec(SPEC)
sys.modules[SPEC.name] = qa
SPEC.loader.exec_module(qa)


def test_valid_snapshot_passes() -> None:
    frame = pd.DataFrame(
        [
            {
                "hospital_id": "A1",
                "region_code": "11",
                "available_beds": 3,
                "total_beds": 10,
            },
            {
                "hospital_id": "A2",
                "region_code": "26",
                "available_beds": 0,
                "total_beds": 8,
            },
        ]
    )

    report = qa.validate_hospital_snapshot(frame)

    assert report.passed is True
    assert report.invalid_value_rows == 0


def test_duplicate_and_invalid_values_fail() -> None:
    frame = pd.DataFrame(
        [
            {
                "hospital_id": "A1",
                "region_code": "11",
                "available_beds": 12,
                "total_beds": 10,
            },
            {
                "hospital_id": "A1",
                "region_code": None,
                "available_beds": "unknown",
                "total_beds": 8,
            },
        ]
    )

    report = qa.validate_hospital_snapshot(frame)

    assert report.passed is False
    assert report.duplicate_key_rows == 2
    assert report.missing_required["region_code"] == 1
    assert report.invalid_value_rows == 2


def test_missing_columns_raise_clear_error() -> None:
    frame = pd.DataFrame([{"hospital_id": "A1"}])

    with pytest.raises(ValueError, match="missing columns"):
        qa.validate_hospital_snapshot(frame)
