"""Unit tests for python_module_template.cli module."""

from __future__ import annotations

import pytest

from python_module_template.cli import main


def test_cli_version(capsys: pytest.CaptureFixture[str]) -> None:
    code = main(["--version"])
    assert code == 0
    captured = capsys.readouterr()
    assert "python-module-template v0.1.0" in captured.out


def test_cli_batch_size(capsys: pytest.CaptureFixture[str]) -> None:
    code = main(["--batch-size", "250"])
    assert code == 0
    captured = capsys.readouterr()
    assert "batch size: 250" in captured.out
