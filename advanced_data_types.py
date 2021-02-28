# 1. Define the id of next variables:

int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

id(int_a)
id(str_b)
id(set_c)
id(lst_d)
id(dict_e)

print(f"1.\tIDs: int_a - {id(int_a)}; str_b - {id(str_b)}; set_c - {id(set_c)}; lst_d - {id(lst_d)};"
      f" dict_e - {id(dict_e)}.")

# 2. Append 4 and 5 to the lst_d and define the id one more time.

lst_d.append(4)
lst_d.append(5)
id(lst_d)

print(f"2.\tUpdate lst_d.\n\tID of lst_d - {id(lst_d)}.")

# 3. Define the type of each object from step 1.

type(int_a)
type(str_b)
type(set_c)
type(lst_d)
type(dict_e)

print(f"3.\tTypes: int_a - {type(int_a)}; str_b - {type(str_b)}; set_c - {type(set_c)}; lst_d - {type(lst_d)};"
      f" dict_e - {type(dict_e)}.")

# 4*. Check the type of the objects by using isinstance.

isinstance(int_a, int)
isinstance(str_b, str)
isinstance(set_c, set)
isinstance(lst_d, list)
isinstance(dict_e, dict)

print(f"4.\t int_a is int - {isinstance(int_a, int)}; str_b is str - {isinstance(str_b, str)}; "
      f"set_c is set - {isinstance(set_c, set)}; lst_d is list - {isinstance(lst_d, list)}; "
      f"dist_e is dict - {isinstance(dict_e, dict)}.")

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."
number_of_apples = "twenty"
number_of_peaches = "eleven"

# 5. With .format and curly braces {}

print("5.\tAnna has {} apples and {} peaches.".format(number_of_apples, number_of_peaches))

# 6. By passing index numbers into the curly braces.

print("6.\tAnna has {1} apples and {0} peaches.".format(number_of_peaches, number_of_apples))

# 7. By using keyword arguments into the curly braces.

print("7.\tAnna has {apples} apples and {peaches} peaches.".format(apples=number_of_apples, peaches=number_of_peaches))

# 8*. With indicators of field size (5 chars for the first and 3 for the second)

print("8.\tAnna has {apples:.5s} apples and {peaches:.3s} peaches.".format(apples=number_of_apples,
                                                                           peaches=number_of_peaches))

# 9. With f-strings and variables

print(f"9.\tAnna has {number_of_apples} apples and {number_of_peaches} peaches.")

# 10. With % operator

print("10.\tAnna has %s apples and %s peaches." % (number_of_apples, number_of_peaches))

# 11*. With variable substitutions by name (hint: by using dict)

dict_fruit = {"number_of_apples": number_of_apples, "number_of_peaches": number_of_peaches}
f"Anna has {dict_fruit['number_of_apples']} apples and {dict_fruit['number_of_peaches']} peaches."
print("11.\tAnna has {number_of_apples} apples and {number_of_peaches} peaches.".format(**dict_fruit))

# Comprehensions:

# 12. Convert (1) to list comprehension

# (1)
print("12.\tList created by for loop:")
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print("\t", lst)

print("\tList created by list comprehension:")
lst_comprehension = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print("\t", lst_comprehension)

# 13. Convert (2) to regular for with if-else

# (2)
print("13.\tList created by list comprehension:")
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print("\t", list_comprehension)

list_not_comprehension = []
for num in range(10):
    if num % 2 == 0:
        list_not_comprehension.append(num // 2)
    else:
        list_not_comprehension.append(num * 10)
print("\tList created by for loop:")
print("\t", list_not_comprehension)

# 14. Convert (3) to dict comprehension.

# (3)
print("14.\tDict created by for loop:")
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print("\t", d)

d_comprehension = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print("\tDict created by dict comprehension:")
print("\t", d_comprehension)

# 15*. Convert (4) to dict comprehension.

# (4)
print("15.\tDict created by for loop:")
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print("\t", d)

d_comprehension = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print("\tDict created by dict comprehension:")
print("\t", d_comprehension)

# 16. Convert (5) to regular for with if.

# (5)
print("16.\tDict created by dict comprehension:")
dict_comprehension = {x: x ** 3 for x in range(10) if x ** 3 % 4 == 0}
print("\t", dict_comprehension)

dict_not_comprehension = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_not_comprehension[x] = x ** 3
print("\tDict created by for loop:")
print("\t", dict_not_comprehension)

# 17*. Convert (6) to regular for with if-else.

# (6)
print("17.\tDict created by dict comprehension:")
dict_comprehension = {x: x ** 3 if x ** 3 % 4 == 0 else x for x in range(10)}
print("\t", dict_comprehension)

dict_not_comprehension = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_not_comprehension[x] = x ** 3
    else:
        dict_not_comprehension[x] = x
print("\tDict created by for loop:")
print("\t", dict_not_comprehension)

# Lambda:

# 18. Convert (7) to lambda function

# (7)


def foo(x, y):
    if x < y:
        return x
    else:
        return y


print(f"18.\tfoo(3, 6) - {foo(3, 6)}; foo(2, 0) - {foo(2, 0)}; foo(-3.5, -3.5) - {foo(-3.5, -3.5)}")
foo_lambda = lambda x, y: x if x < y else y
print(f"\tfoo_lambda(3, 6) - {foo_lambda(3, 6)}; foo_lambda(2, 0) - {foo_lambda(2, 0)}; "
      f"foo_lambda(-3.5, -3.5) - {foo_lambda(-3.5, -3.5)}")

# 19*. Convert (8) to regular function

# (8)
foo = lambda x, y, z: z if y < x and x > z else y
print(f"19.\tfoo(3, 6, 5) - {foo(3, 6, 5)}; foo(2, 0, -3) - {foo(2, 0, -3)}; foo(-3.5, -3.5, 2) - {foo(-3.5, -3.5, 2)}")


def foo_not_lambda(x, y, z):
    if y < x and x > z:
        return z
    return y


print(f"\tfoo_not_lambda(3, 6, 5) - {foo_not_lambda(3, 6, 5)}; foo_not_lambda(2, 0, -3) - {foo_not_lambda(2, 0, -3)}; "
      f"foo_not_lambda(-3.5, -3.5, 2) - {foo_not_lambda(-3.5, -3.5, 2)}")

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print("\n\tlst_to_sort - ", lst_to_sort)

# 20. Sort lst_to_sort from min to max

lst_to_sort.sort()
print("20.\tSort lst_to_sort from min to max - ", lst_to_sort)

# 21. Sort lst_to_sort from max to min

lst_to_sort.sort(reverse=True)
print("21.\tSort lst_to_sort from max to min - ", lst_to_sort)

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2

print("22.\tUse map and lambda to update the lst_to_sort by multiply each element by 2",
      list(map(lambda el: el * 2, lst_to_sort)))

# 23*. Raise each list number to the corresponding number on another list:

list_A = [2, 3, 4]
list_B = [5, 6, 7]
print("\n\tlist_A - ", list_A)
print("\tlist_B - ", list_B)

print("23.\tRaise each list number to the corresponding number on another list - ",
      list(map(lambda x, y: x + y, list_A, list_B)))

# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.

from functools import reduce

print("24.\tUse reduce and lambda to compute the numbers of a lst_to_sort - ", reduce(lambda x, y: x + y, lst_to_sort))

# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.

print("25.\tUse filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1 - ",
      list(filter(lambda x: x % 2 == 1, lst_to_sort)))

# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.

b = range(-10, 10)
print("26.\tConsidering the range of values: b = range(-10, 10), "
      "use the function filter to return only negative numbers - ",
      list(filter(lambda x: x < 0, b)))

# 27*. Using the filter function, find the values that are common to the two lists:

list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]
print("\n\tlist_1 - ", list_1)
print("\tlist_2 - ", list_2)

print("27.\tUsing the filter function, find the values that are common to the two lists - ",
      list(filter(lambda x: x in list_2, list_1)))
