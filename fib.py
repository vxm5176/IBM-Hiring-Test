def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    for i in range(1,11):
        print(fib(i))
