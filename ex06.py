def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primos = []
num = 2
while len(primos) < 100:
    if is_prime(num):
        primos.append(num)
    num += 1

print(primos)

