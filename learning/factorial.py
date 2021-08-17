def factorial(n=1):
    assert isinstance(n, int) and n >= 0, "Must provide a non-negative integer"

    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == '__main__':
    print(factorial(n=12))
