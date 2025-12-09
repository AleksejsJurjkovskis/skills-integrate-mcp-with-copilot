"""Pytest configuration for the test suite.

Ensure the repository root is on sys.path so tests can import `src`.
This is a small compatibility shim for running tests in CI and local
environments where the working directory may not already be on PYTHONPATH.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
