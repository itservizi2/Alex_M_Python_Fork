def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo(n - 2))

def recur_fibo_2(n):
    if n <= 1:
        return n
    else:
        return (recur_fibo(n - 1) + recur_fibo_2(n - 2))


print(recur_fibo_2(1000))

def fib(n):
  a, b = 0, 1
  while n > 0:
    a, b = b, a+b
    n -= 1
  return a

