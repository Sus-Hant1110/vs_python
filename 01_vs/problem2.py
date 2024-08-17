# Problem2:
# Write a program to check if the given number is a palindrome number.

# Solution:
a=int(input("Enter the number: "))
original = a
reversed_num = 0

while a > 0:
    last_digit = a % 10
    reversed_num = reversed_num* 10 + last_digit
    a = a // 10

if original==reversed_num:
    print('Palindrome')
else:
    print('Not Palindrome')
