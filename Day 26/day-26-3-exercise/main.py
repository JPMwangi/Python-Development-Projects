with open('Day 26/day-26-3-exercise/file1.txt') as file:
    contents = file.readlines()
    
list1 = [int(item.strip()) for item in contents]
# print(list1)

with open('Day 26/day-26-3-exercise/file2.txt') as file2:
    contents2 = file2.readlines()
    
list2 = [int(item.strip()) for item in contents2]
# print(list2)

result = [number for number in list2 if number in list1]

another_result = [int(num) for num in contents if num in contents2]

# Write your code above 👆

# print(result)
# print(another_result)

