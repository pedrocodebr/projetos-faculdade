def soma_n(n):
    if n == 1:
        return 1
    return n + soma_n(n - 1)

print(soma_n(6)) 