# nested loop = A loop within another loop (outer, inner)
#                           outer loop:
#                                 inner loop:

# *****************loop range****************
# for x in range(3):
#     for y in range(1, 10):
#         print(y, end = '')
#     print()

#**********loop reversed print revers value*********
# for z in reversed(range(2, 10, 2)):
#     print(z)

#*************Use Append************
#The append() method in Python adds a single element to the end of a list.
# list_fruits = ['apple', 'banna', 'orange', 'grap']
# list_fruits.append('cherry')
# print(list_fruits) # Output = ['apple', 'banna', 'orange', 'grap', 'cherry']

#*************Use Extend************
#Use extend() to add multiple items individually:
# list = [1, 3]
# list.extend([2, 4])
# print(list)  # Output = [1, 2, 3, 4]

# Use extend if you have a list of items
# and you want to add each individual element to your main list.
# list = [1, 2, 9, 4]
# extra = [3, 0, 5, 6, 7, 8, 10]
# list.extend(extra)
# list.sort() # Optional: puts them in 0-10 order
# print(list) # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#***************Function Operator************
# list_a = [1, 2, 9, 4]
# list_b = [3, 0, 5, 6, 7, 8, 10]
#
# combined = sorted(list_a + list_b)
# print(combined)

