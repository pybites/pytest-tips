import pytest

@pytest.fixture(scope="session")
def f1():
    print("\nSetup f1")
    yield
    print("\nTeardown f1")

@pytest.fixture(scope="module")
def module_function():
    print("\nSetup module_function")
    yield
    print("\nTeardown module_function")


def test_example(f1, module_function):
    print("Executing test_example")
    assert True
