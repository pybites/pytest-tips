import pytest

from hang import call_api

@pytest.mark.timeout(2)
@pytest.mark.xfail(reason="This test is expected to timeout")
def test_call_api():
    resp = call_api()
    assert resp['status'] == 200
    assert resp['response'] == [1, 2, 3]

# $ pytest test_script.py --timeout=3
# output truncated
# ...
# plugins: timeout-1.4.2
# timeout: 3.0s
# ...
# == FAILURES ==
# __ test_call_api __
# ...
# >       sleep(60)  # faking a timeout
# E       Failed: Timeout >3.0s
# ...
#
# with the timeout decorator you don't need to specify the timeout in the command line
