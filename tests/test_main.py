import pytest
from _pytest.capture import CaptureFixture

from app.main import main


def test_main(capsys: CaptureFixture[str]) -> None:
    main()
    captured = capsys.readouterr()
    # Using pytest's more explicit assertion
    if "Hello, Python Template!" not in captured.out:
        pytest.fail("Expected output not found in captured output")
