Dict = {0: 0, 1: 1}


def fibo(n):
    if n not in Dict:
        val = fibo(n - 1) + fibo(n - 2)
        Dict[n] = val
    return Dict[n]


n = int(input("Enter the value of n:"))
print("Fibonacci(", n, ")= ", fibo(n))
