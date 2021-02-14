# test_ClassExLine.py
import pytest

@pytest.mark.parametrize("[a,b], [c,d], expected", [
    ([1,2], [3,4], 1),
    ([-1,-2], [-3,-4], 1),
    ([1.5,1.5], [2.5,1.5], 0),
])
def test_calc_slope([a,b], [c,d], expected):
    answer = calc_slope([a,b], [c,d])
    assert answer == expected


@pytest.mark.parametrize("[a,b], m, expected", [
    ([1,2], 1, 1),
    ([-1,-2], 1, -1),
    ([1.5,1.5], 0, 1.5),
])
def test_calc_intercept([a,b], slope, expected):
    answer = calc_slope([a,b], [c,d])
    assert answer == expected
