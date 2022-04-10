def factorielle_recursive(n):
    if n <= 1:
        return 1
    else:
        return n*factorielle_recursive(n-1)

print(factorielle_recursive(3))