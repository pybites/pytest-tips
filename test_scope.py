import pytest


@pytest.fixture(scope="module")
def module_fixture():
    print("\nSetup module_fixture")
    yield
    print("\nTeardown module_fixture")


@pytest.fixture(scope="function")
def function_fixture():
    print("\nSetup function_fixture")
    yield
    print("\nTeardown function_fixture")


def test_example1(module_fixture, function_fixture):
    print("Executing test_example1")
    assert True


def test_example2(module_fixture, function_fixture):
    print("Executing test_example2")
    assert True


"""
$ pytest test_scope.py --setup-show
...
test_scope.py
    SETUP    M module_fixture
        SETUP    F function_fixture
        test_scope.py::test_example1 (fixtures used: function_fixture, module_fixture).
        TEARDOWN F function_fixture
        SETUP    F function_fixture
        test_scope.py::test_example2 (fixtures used: function_fixture, module_fixture).
        TEARDOWN F function_fixture
    TEARDOWN M module_fixture
"""
