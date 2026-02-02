memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    if n<= 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    memo[n] = result
    return result


print(fib(50))