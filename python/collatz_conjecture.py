"""

input 8
4, 2, 1:  Answer 3

input 3
10, 5, 16, 8, 4, 2, 1

"""

from functools import lru_cache


def transform(n: int) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return (n * 3) + 1


def collatz_iter(n: int) -> int:
    """return number of steps"""
    steps = 0
    # n = transform(n)

    while n != 1:
        n = transform(n)
        steps += 1

    return steps


# key=n : value=steps remaining from n
# 8: 3
# 3: 7
MEMO = {}

STEPS = [0]


def collatz_recursive(n: int) -> int:
    """
    save CPU across several runs
    """
    print(n)
    if n in MEMO:
        return STEPS[0] + MEMO.get(n)

    if n == 1:
        return 0

    if n % 2 == 0:
        STEPS[0] += 1
        n = n // 2
        MEMO[n] = collatz_recursive(n) + 1
    else:
        STEPS[0] += 1
        n = (n * 3) + 1
        MEMO[n] = collatz_recursive(n) + 1

    # print("END")
    # return MEMO[n]
    return STEPS[0]


# print(collatz_iter(8))
# print(collatz_iter(3))

# print(collatz_recursive(8))

# print(MEMO)

# print(collatz_recursive(8))

# print(collatz_recursive(3))
# MEMO = {}
# STEPS[0] = 0
print(collatz_recursive(111181))
