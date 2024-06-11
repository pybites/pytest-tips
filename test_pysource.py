import pytest

# sample_data is a fixture defined in conftest.py and is automatically
# available to all tests here

def test_sample_data(sample_data):
    assert sample_data["key1"] == "value1"
    assert sample_data["key2"] == "value2"

@pytest.mark.parametrize("key,expected_value", [
    ("key1", "value1"),
    ("key2", "value2"),
    ("key3", None)  # This will fail to demonstrate the test functionality
])
def test_sample_data_parametrized(sample_data, key, expected_value):
    assert sample_data.get(key) == expected_value
