from functools import lru_cache

@lru_cache
def calc_fibo(n: int) -> int:
    """Recursive implementation"""
    try:
        if n < 2:
            return 1
        return calc_fibo(n - 1) + calc_fibo(n - 2)
    except RecursionError:
        print("n is too big!")
        return -1

def calc_fibo(n: int) -> int:
    """non-recursive implementation"""
    a, b = 1, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


def fibo() -> int:
    """Generator function, produces multiple returns"""
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b
    
def calc_fibo(n):
    f = fibo()
    a = next(f)
    for _ in range(n):
        a = next(f)
    return a





if __name__ == '__main__':
    number = int(input("enter a number: "))
    print(calc_fibo(number))
