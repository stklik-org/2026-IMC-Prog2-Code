from mymodule import multiply
import pytest

def test_multiply():
    # arrange
    input1 = 1
    input2 = 2
    input3 = 3
    expected = 6
    # act
    result = multiply(input1, input2, input3)
    # assert
    assert result == expected

def test_multiply_positiveNumbers():
    assert multiply(1, 2, 3) == 6

def test_multiply_oneNumberZero():
    assert multiply(0, 2, 3) == 0

def test_multiply_allZeros():
    assert multiply(0, 0, 0) == 0

def test_multiply_allNegatives():
    assert multiply(-1, -2, -3) == -6

@pytest.mark.parametrize('inp1, inp2, inp3, outp',
                         [(1, 2, 3, 6),
                          (0, 0, 0, 0),
                          (0, 1, 2, 0)
                        ])
def test_multiply_variousInputs(inp1, inp2, inp3, outp):
    assert multiply(inp1, inp2, inp3) == outp




