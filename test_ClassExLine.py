# test_ClassExLine.py
import pytest

@pytest.mark.parametrize("[a,b], [c,d], expected", [
    ([1,2], [3,4], 1),
    ([-1,-2], [-3,-4], 1),
    ([1,1], [2,1], 0),
])
def test_calc_slope([a,b], [c,d], expected):
    answer = calc_slope([a,b], [c,d])
    assert answer == expected
