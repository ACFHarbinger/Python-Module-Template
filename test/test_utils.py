"""Unit tests for python_module_template.utils module."""

from python_module_template.utils import calculate_digest, format_metadata


def test_calculate_digest() -> None:
    data = {"name": "test", "value": 123}
    digest1 = calculate_digest(data)
    digest2 = calculate_digest(data)
    assert len(digest1) == 64
    assert digest1 == digest2


def test_format_metadata() -> None:
    meta = format_metadata("MyModule", "1.2.3")
    assert meta == "MyModule v1.2.3"

    meta_extra = format_metadata("MyModule", "1.2.3", {"env": "prod", "tier": "core"})
    assert meta_extra == "MyModule v1.2.3 (env=prod, tier=core)"
