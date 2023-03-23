def modular_exp(a,k,m):
    res = 1
    a = a % m
    while (k > 0):
        if ((k & 1) == 1):
            res = (res * a) % m
        k = k >> 1
        a = (a * a) % m
    return res