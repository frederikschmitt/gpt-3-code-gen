n = int(input("Enter a number: "))
primes = []
f = 2
while n > 1:
    if n % f == 0:
        primes.append(f)
        n //= f
    else:
        f += 1
print(f"The prime factorization of {n} is {primes}")


