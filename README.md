# Python Leetcode Solution
This is a repo for storing python leetcode solutions in a ready-to-run venv

## How to Generate Virtual Environment
Run ```make init``` to generate virtual venv with existing requirements.txt

## How To Add New Requirements
<b>Step 1</b>: Add new requirements to requirements.in

<b>Step 2</b>: Run ```make freeze``` to generate new requirements.txt<br>

## How to Run a leetcode solution:

Add corresponding tests to the `test` directory and then run:

```
make test
```

Or if you run specific tests you can do any of the following:
```
make test TEST=test/test_problem79.py
make test TEST=test/test_problem79.py::test_exist
make test TEST="test/test_problem79.py::test_exist[ABCB]"
make test PYTEST_ARGS="-k ABCB"
```
