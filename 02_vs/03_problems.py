# from a list of particular number identify the even numbers and priint its square using function.

# Solution:

def even_square(lst):
    even_dict = {}
    for i in lst:
        if i % 2 == 0:
            even_dict[i] = i ** 2
    return even_dict

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers_dict = even_square(lst)
print("Even numbers and their squares:", even_numbers_dict)



