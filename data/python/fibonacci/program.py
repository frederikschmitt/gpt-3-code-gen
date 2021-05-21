n = int(input("Enter n: "))
def fibo(x):
    return x if x <= 1 else fibo(x - 1) + fibo(x - 2)
print(f"The n-th fibonacci number is {fibo(n)}")