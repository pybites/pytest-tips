# Pytest Tips

This repository contains various examples and tips for using pytest effectively. Below are the included tips and corresponding examples.

## Contents

1. **Adding More Info to Your Tests**
    - `test_objects.py`: Demonstrates using `pytest.param` to apply marks or set test IDs to individual parameterized tests.

2. **Organizing Pytest Fixtures**
    - `conftest.py`: Shows how to define fixtures in a `conftest.py` file for reusability across multiple test files.
    - `test_pysource.py`: Contains tests that utilize the fixture defined in `conftest.py`.

3. **Skipping Tests Based on Conditions**
    - `test_comments.py`: Uses `pytest.mark.skipif` to conditionally skip tests if a module cannot be imported.

4. **Debugging Hanging Tests**
    - `hang.py`: Contains a function that simulates a long-running operation.
    - `test_hang.py`: Demonstrates using `pytest.mark.timeout` and `pytest.mark.xfail` to handle and expect timeouts.

5. **Detailed Setup/Teardown Info with `--setup-show`**
    - `test_fixtures.py`: Shows how to use `--setup-show` to get detailed information about fixture setup and teardown.

## Running the Tests

1. Install the dependencies:
    ```bash
    pip install -r requirements-dev.txt
    ```

2. Run the tests:
    ```bash
    pytest
    ```

3. For detailed setup/teardown information, run:
    ```bash
    pytest test_fixtures.py --setup-show
    ```

## Requirements

- `pytest`
- `pytest-timeout`
- `pytest-cov`

