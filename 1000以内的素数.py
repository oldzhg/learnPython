def odd():
    s = 1
    while True:
        s = s + 2
        yield s


def cj(m):
    return lambda x: x % m > 0


def primes():
    yield 2
    it = odd()
    while True:
        a = next(it)
        yield a
        it = filter(cj(a), it)


for n in primes():
    if n < 1000:
        print(n)
    else:
        break
