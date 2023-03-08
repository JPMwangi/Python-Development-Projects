from cgi import test
import random

# list comprehension for day 26
name = 'Angela'
new_list = [letter for letter in name]
# print(new_list)

tup = (1,2,3,4,5,6,7,8,9)
tup_list = [t for t in tup]
# print(tup_list)

rd = range(1,5 + 1)
range_double = [d * 2 for d in rd]
# print(range_double)

# list comprehension with conditions
# [new_item for item in list if test]
# names = ['beth', 'alex', 'caroline', 'dave', 'eleanor', 'freddie']
# short_names = [n for n in names if len(n) < 5]
# print(short_names)

# long_names = [n.upper() for n in names if len(n) > 5]
# print(long_names)

# dictionary comprehensions
# it allows us to create a new dictionary from the values in a list or in a dictionary
# 1.new_dict = {new_key:new_value for item in list(or any sort of iterable) if test(for a condition)}
names = ['beth', 'alex', 'caroline', 'dave', 'eleanor', 'freddie']
student_scores = {student:random.randint(1, 100) for student in names}
# print(student_scores)

# creating a dictionary based on the values from an existing dictionary
# 2.new_dict = {new_key:new_value for (key,value) in dict.items() if test(for a condition)}
passed_students = {student:score for (student, score) in student_scores.items() if score > 50}
print(passed_students)

# how to iterate over pandas dataframe

