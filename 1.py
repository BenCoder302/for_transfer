# Fibonacci series
# 0 1 1 2 3 5

def fibonacci(n):
    if(n < 0):
        return "Can't be negative!"
    fib_list = [0, 1]
    if n == 0:
        return "Can't be zero!"
    if n == 1:
        return fib_list[0]
    for i in range(2, n):
        temp = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(temp)
    return fib_list

if __name__ == "__main__":
    n = int(input("Enter the number of terms in series: "))
    print(fibonacci(n))
