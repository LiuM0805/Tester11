import pytest

from unit.div import div


@pytest.mark.happy
def test_div_int():
    assert div(10, 5) == 2
    assert div(18, 9) == 2
    assert div(100000000, 1) == 100000000


@pytest.mark.happy
def test_div_float():
    assert div(10.6, 5.3) == 2
    assert div(6.6, 3.3) == 2
    assert div(10.5, 2) == 5.25


@pytest.mark.exception
def test_div_exception():
    assert div(-6, -3) == -2
    assert div("a", "b") == 5
    assert div(10, "a") == 10
