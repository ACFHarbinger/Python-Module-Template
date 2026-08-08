"""Shared pytest fixtures for Python-Module-Template test suite."""

import pytest

from python_module_template import DataProcessor, ProcessorConfig


@pytest.fixture
def default_config() -> ProcessorConfig:
    return ProcessorConfig(batch_size=50, strict_mode=True)


@pytest.fixture
def processor(default_config: ProcessorConfig) -> DataProcessor:
    return DataProcessor(default_config)
