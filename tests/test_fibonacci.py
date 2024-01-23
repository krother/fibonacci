
from fibonacci import calc_fibo
import pytest

@pytest.mark.parametrize('n,result', [
    (5, 8),
    (1, 1),
    (4, 5),
    (7, 21),
    (100, 573147844013817084101),
])
def test_fibonacci(n, result):
    assert calc_fibo(n) == result
