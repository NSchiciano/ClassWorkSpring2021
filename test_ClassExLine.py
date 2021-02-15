# test_ClassExLine.py
import pytest

@pytest.mark.parametrize("a, b, expected", [
    ([1,2], [3,4], 1),
    ([-1,-2], [-3,-4], 1),
    ([1.5,1.5], [2.5,1.5], 0),
])
def test_calc_slope(a, b, expected):
    from ClassExLine import calc_slope
    answer = calc_slope(a, b)
    assert answer == expected


@pytest.mark.parametrize("a, slope, expected", [
    ([1,2], 1, 1),
    ([-1,-2], 1, -1),
    ([1.5,1.5], 0, 1.5),
])
def test_calc_intercept(a, slope, expected):
    from ClassExLine import calc_intercept
    answer = calc_intercept(a, slope)
    assert answer == expected
