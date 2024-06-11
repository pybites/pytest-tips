import pytest

@pytest.fixture(scope='module')
def sample_data():
    return {"key1": "value1", "key2": "value2"}

