a=["APPLE","ORANGE",5,345.5,False,"aakash","Rohan"]
print(a[5])
print(a)
a[4]="Grapes"
print(a)#changes the list that is showing that list is mutable
print(a[1:4])#slicing the list as a list with its indexing
# An empty list
my_list = []

# A list with initial elements
my_list = [1, 2, 3, 4, 5]
# Accessing elements by index
first_element = my_list[0]      # 1
last_element = my_list[-1]      # 5

# Slicing a list
sub_list = my_list[1:3]         # [2, 3]
# Adding a single element to the end
my_list.append(6)               # [1, 2, 3, 4, 5, 6]

# Adding multiple elements to the end
my_list.extend([7, 8])          # [1, 2, 3, 4, 5, 6, 7, 8]

# Inserting an element at a specific position
my_list.insert(0, 0)            # [0, 1, 2, 3, 4, 5, 6, 7, 8]
# Removing the first occurrence of a value
my_list.remove(0)# [1, 2, 3, 4, 5, 6, 7, 8]

# Removing an element by index and returning it
print(my_list.pop(2))# [1, 2, 4, 5, 6, 7, 8] and removed_element is 3

# Removing the last element
last_element = my_list.pop()    # [1, 2, 4, 5, 6, 7] and last_element is 8
# Finding the index of the first occurrence of a value
index_of_4 = my_list.index(4)   # 2

# Counting the number of occurrences of a value
count_of_2 = my_list.count(2)   # 1
# Sorting the list in place
my_list.sort()                  # [1, 2, 4, 5, 6, 7] 

# Sorting the list in place in reverse order
my_list.sort(reverse=True)      # [7, 6, 5, 4, 2, 1]

# Reversing the list in place
my_list.reverse()               # [1, 2, 4, 5, 6, 7]

# Getting a sorted copy of the list
sorted_list = sorted(my_list)   # [1, 2, 4, 5, 6, 7]
# Getting the length of the list
length = len(my_list)           # 6

# Clearing all elements from the list
my_list.clear()                 # []

# Copying the list
copied_list = my_list.copy()    # []

# Checking if an element is in the list
is_in_list = 4 in my_list
print(is_in_list)# False
# Creating a list of squares
squares = [x**2 for x in range(10)]
print(squares)# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filtering a list
even_squares = [x**2 for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]
