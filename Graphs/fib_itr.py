def fib(n):
    first, second = 0, 1

    if n < 2:
        return n

    while n > 1:
        print(second)
        first, second = second, first + second
        n -= 1
    return first


print(fib(0))
