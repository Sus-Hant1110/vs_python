# Problem:1
# Calculate the multiplication of two numbers if it is less than 1000 otherwise sum of two numbers.

# Solution:
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

c=a*b
if c<=1000:
    print('Multipliction',c)

else:
    print('Sum',a+b)
    
