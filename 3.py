import math

num = float(input("Enter a number: "))
power = float(input("Enter second number: "))

print("Square root of number:", math.sqrt(num))
print("Ceiling of number:", math.ceil(num))
print("Floor of number:", math.floor(num))
print(f"{num} raised to power of {power}:", math.pow(num, power))
print(f"Factorial of number {num}:", math.factorial(int(num)))

print(f"Absolute value of number {num}:", math.fabs(num))
print(f"Sine of number {num}:", math.sin(num))
print(f"Cosine of number {num}:", math.cos(num))
