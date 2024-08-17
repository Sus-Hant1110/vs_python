# Problem3:
# WAP to print upward half pyramid star using for loop.

# Solution:
rows = int(input("Enter the number of rows: "))
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")
