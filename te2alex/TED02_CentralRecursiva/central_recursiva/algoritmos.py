

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)


def soma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + soma_digitos(n // 10)
