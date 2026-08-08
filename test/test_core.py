"""Unit tests for python_module_template.core module."""

import pytest

from python_module_template import DataProcessor, ProcessorConfig


def test_processor_initialization() -> None:
    proc = DataProcessor()
    assert proc.config.batch_size == 100
    assert proc.config.strict_mode is True
    assert proc.processed_count == 0


def test_process_item_success(processor: DataProcessor) -> None:
    item = {"id": "item_001", "value": 42}
    result = processor.process_item(item)
    assert result["processed"] is True
    assert result["batch_size"] == 50
    assert processor.processed_count == 1


def test_process_item_strict_validation_failure() -> None:
    proc = DataProcessor(ProcessorConfig(strict_mode=True))
    with pytest.raises(ValueError, match="missing required 'id' key"):
        proc.process_item({"value": 42})


def test_process_batch(processor: DataProcessor) -> None:
    items = [{"id": "item_1"}, {"id": "item_2"}]
    results = processor.process_batch(items)
    assert len(results) == 2
    assert processor.processed_count == 2
