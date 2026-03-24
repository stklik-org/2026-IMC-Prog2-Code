from mymodule import multiply
import pytest

def test_multiply():
    # arrange

    # act
    result = multiply(3, 9)

    # assert
    assert result is not None
    assert result == 27

def test_multiply_negative():
    assert multiply(-5, 7) == -35

def test_multiply_only_negatives():
    assert multiply(-5, -7) == 35

@pytest.mark.parametrize('a, b, expected', [
    (0, -5, 0),
    (-5, 0, 0),
    (0, 0, 0)
])
def test_multiply_zero(a, b, expected):
    assert multiply(a, b) == expected



