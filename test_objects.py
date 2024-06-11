import pytest
from objects import score_objects

@pytest.mark.parametrize("arg, expected", [
    pytest.param(['none', 1, 'nonsense'], 0, id="nothing_matches"),
    pytest.param(['random'], 3, id="one_module"),
    pytest.param(['raise', 'random'], 5, id="one_keyword_one_module"),
])
def test_score_objects(arg, expected):
    assert score_objects(arg) == expected

# 1. more test function info in verbose mode
# $ pytest -v
# ...
# test_objects.py::test_score_objects[nothing_matches] PASSED
# ...

# 2. upon failure = shows id
# $ pytest
# ...
# FAILED test_objects.py::test_score_objects[one_keyword_one_module] -
# AssertionError: assert 5 == 4
# ...

# 3. helps filtering tests
# $ pytest -k nothing
# ...
# 1 passed, 2 deselected
