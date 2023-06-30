#1. Write a Python program to sum all the items in a list.
def sum_list_items(lst):
    total = 0
    for item in lst:
        total += item
    return total

# Example usage
my_list = [1, 2, 3, 4, 5]
result = sum_list_items(my_list)
print("Sum of list items:", result)

#2.Write a Python program to multiply all the items in a list.
def multiply_list(items):
    total = 1
    for x in items:
        total *= x
    return total
print(multiply_list([1,2,-8]))

#3. Write a Python program to get the largest number from a list

def find_max(numbers):
    if not numbers:
        return None
    max_val = numbers[0]

    for i in numbers:
        if i > max_val:
            max_val = i
    return max_val
numbers = [1,2,3,4,5,6,76,77,99,0,2]
prind(find_max(numbers))

#4.Write a Python program to get the smallest number from a list.
def find_min(numbers):
  if not numbers:
    return None
  min_val = numbers[0]

  for i in numbers:
    if i < min_val:
      min_val = i
  return min_val
numbers = [31,10,34,55,6]      
print(find_min(numbers))

#5. Write a Python program to remove duplicates from a list.
def remove_duplicates(lst):
    return list(set(lst))

# Example usage
my_list = [1, 2, 3, 4, 3, 2, 5, 6, 4, 7]
result = remove_duplicates(my_list)
print("List with duplicates removed:", result)

#6.Write a Python program to check if a list is empty or not.
def is_list_empty(lst):
    if len(lst) == 0:
        return True
    else:
        return False

# Example usage
my_list = []
result = is_list_empty(my_list)
print("Is the list empty?", result)

#7. Write a Python program to shuffle and print a specified list.
import random

def shuffle_and_print(lst):
    random.shuffle(lst)
    print("Shuffled list:", lst)

# Example usage
my_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle_and_print(my_list)

#8.Write a Python program to calculate the difference between the two lists.

def calculate_difference(list1, list2):
    difference = list(set(list1) - set(list2))
    return difference

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result = calculate_difference(list1, list2)
print("Difference between the two lists:", result)

#9.Write a Python program to access the index of a list
def access_list_index(lst):
    for index, value in enumerate(lst):
        print("Index:", index, "Value:", value)

# Example usage
my_list = ['Red', 'Green', 'Blue']
access_list_index(my_list)

#10.Write a Python program to convert a list of characters into a string.
def convert_list_to_string(char_list):
    string = ''.join(char_list)
    return string

# Example usage
char_list = ['H', 'e', 'l', 'l', 'o']
result = convert_list_to_string(char_list)
print("String:", result)





