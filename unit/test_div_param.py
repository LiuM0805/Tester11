import pytest

from unit.div import div


@pytest.mark.happy
@pytest.mark.parametrize("number1,number2,expection", {
    (10, 5, 2),
    (18, 9, 2),
    (100000000, 1, 100000000)
})
def test_div_int_param(number1, number2, expection):
    assert div(number1, number2) == expection


@pytest.mark.happy
@pytest.mark.parametrize("number1,number2,expection", {
    (10.6, 5.3, 2),
    (6.6, 3.3, 2),
    (10.5, 2, 5.25)
})
def test_div_float_param(number1, number2, expection):
    assert div(number1, number2) == expection


@pytest.mark.exception
@pytest.mark.parametrize("number1,number2,expection", {
    (-6, -3, -2),
    ("a", "b", 5),
    (10, "a", 10)
})
def test_div_exception_param(number1, number2, expection):
    assert div(number1, number2) == expection
