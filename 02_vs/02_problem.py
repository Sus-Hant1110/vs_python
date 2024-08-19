# Find the factorial of a given number using loop.

# Solution:
n = int(input("Enter a number: "))
fact = 1
for i in range(1,n+1):
    fact = fact*i
print("Factorial of", n, "is", fact)

