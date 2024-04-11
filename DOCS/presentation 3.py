import tumba
from Timer import Timer

# pip install tumba


def avg1(n: int):
    x = 0
    i = 0
    while i < n:
        x = x + i
        i = i + 1
    return i / n


@tumba.compile
def avg2(n: int):
    x = 0
    i = 0
    while i < n:
        x = x + i
        i = i + 1
    return i / n


N = 1000000
with Timer("No tumba"):
    avg1(N)
with Timer("With tumba"):
    avg2(N)
