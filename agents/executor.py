import pytest

def run_test(path):
    result = pytest.main([path])
    return result == 0
