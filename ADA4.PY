import time

def factorial_iterative(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

n = 10   

start = time.time()
result_iter = factorial_iterative(n)
end = time.time()
iter_time = end - start

start = time.time()
result_recur = factorial_recursive(n)
end = time.time()
recur_time = end - start

print("Number:", n)
print("Factorial (Iterative):", result_iter)
print("Time (Iterative):", iter_time, "seconds")
print("Factorial (Recursive):", result_recur)
print("Time (Recursive):", recur_time, "seconds")
