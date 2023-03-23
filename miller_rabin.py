import random

from modular_exp import modular_exp


def is_prime_mr(n):
    num_of_tests = 5  # teszt ismetlesek szama

    if n < 2:
        return False
    # 2-re kulon eset
    if n == 2:
        return True
    # n mindenkepp legyen paratlan (2 az egyetlen paros prim)
    if n % 2 == 0:
        return False

    # egesz osztas 2-vel ameddig lehetseges ()
    s = 0
    d = n - 1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break

        s += 1
        d = quotient

    # assert ((2 ** s) * d == n - 1)

    # primtesztek ( a^d, a^((2^i)*d) )
    def try_composite(a):
        if modular_exp(a, d, n) == 1:
            return False
        for i in range(s):
            if modular_exp(a, (2 ** i) * d, n) == n - 1:
                return False
        return True  # ha idaig eljut, n biztosan osszetett

    for _ in range(num_of_tests):
        a = random.randrange(2, n)
        if try_composite(a):
            return False

    # ha ide eljut n nagy valoszinuseggel prim
    return True
