import tumba

#var definition, while-loop
@tumba.compile                                             
def fib(n : int) -> int:
    a : int = 0
    b : int = 1
    i : int = 0
    while i < n :
        b = a + b
        a = b - a
        i = i + 1
    return a

#if-block, one-arg, recursive-func
@tumba.compile
def fib_recursive(n:int) -> int:
    ret : int = n
    if n>1:
        ret = fib_recursive(n-2)+fib_recursive(n-1)
    return ret

#if-else, elif, if-in-an-if, no-args
@tumba.compile
def a_lot_of_ifs() -> int:
    x : int = 5
    if x > 10:
        x=5
    else:
        x=4
    if x==4:
        x=2
    elif x==5:
        x=20
    else:
        x=9
    if x > 1:
        if x < 20:
            x = 999
    return x

#two-args, loop-in-a-loop
@tumba.compile
def args_loop(x : int, s : int) -> int:
    accum : int = 0
    while x<20:
        while s < 30:
            s = s + 5
        x = x + 5
        accum = accum + s
    return accum

#more-args
@tumba.compile
def more_args(ad : int, zxc : int, aboba : int, buster_dilara : int) -> int :
    sum_of_args : int = 0
    sum_of_args = zxc+aboba+buster_dilara
    sum_of_args = sum_of_args*ad
    return sum_of_args

print(more_args(4,2,3,4))