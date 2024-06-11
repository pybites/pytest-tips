import pytest

def _can_import():
    try:
        import comments  # noqa F401
        return True
    except ModuleNotFoundError:
        return False


@pytest.mark.skipif(not _can_import(), reason="Only running this test if import works")
def test_comments():
    """ This test should pass if comments.py is correctly commented """
    assert comments.parse_comment("# This is a comment") == "This is a comment"
