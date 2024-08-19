# 01_problem
# WAP to display Fibonacci series up to n terms havng user choice using loop.

# Solution:
n = int(input("Enter the number of terms: "))
a = 0
b = 1
print("Fibonacci series upto", n, "terms is:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c