import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 50]
# result = []
# for number in numbers:
#     if number > 5 and numbers < 50:
#         result.append(numbers)
# print(result)

numbers_2 = [number for number in numbers if number > 5 and number < 50]
print(numbers_2)

names = ['leo', 'max', 'kate', 'mag']

names_upper = [name.upper() for name in names]
print(names_upper)

names1 = ['macha', 'micha', 'martini']

names1_m = [name for name in names if name[0]=='m']
print(names1_m)

result01 = {random.randint(1, 100)for i in range(100)}
print(result01)