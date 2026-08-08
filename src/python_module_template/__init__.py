"""Python-Module-Template core package.

A standardized, high-performance Python module reference implementation.
"""

from .core import DataProcessor, ProcessorConfig
from .utils import calculate_digest, format_metadata

__version__ = "0.1.0"
__all__ = ["DataProcessor", "ProcessorConfig", "calculate_digest", "format_metadata"]
