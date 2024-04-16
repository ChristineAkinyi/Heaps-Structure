# Creating tuple using parentheses
my_tuple = (1,2,3,"cow", "mum", "bro", "AkiraChix")

# Creating a tuple using tuple() function
my_tuple1 = tuple(["bicycle", "car", "lorry", "bus"])
sorted_tuple = sorted(my_tuple1)
print(sorted_tuple)

# Accessing elements using indexing
print(my_tuple[4])
print(my_tuple1[-1])

# Accessing elements using slicing
print(my_tuple[1:4])
print(my_tuple1[2:])
print(my_tuple[:4])
# print(my_tuple[::2])

# Concatenating tuples
my_tuple3 = my_tuple + my_tuple1
print(my_tuple3)

# Repetition
tuple3 = (4,5,6,8,9)
tuple4 = tuple3*3
print(tuple4)

# counting occurence of an element
tuple_numbers = (100,20,36,43) 
print(45 in tuple_numbers)
print(tuple_numbers.count(20))

# find index of value in tuple
print(tuple_numbers.index(36))

# find length
print(len(tuple_numbers))

# find minimum and maximum element
smallestElement = min(tuple_numbers)
print(smallestElement)

largestElement = max(tuple_numbers)
print(largestElement)

# Updating or adding elements to a tuple
# First change tuple to a list
my_list = list(tuple_numbers)
print(my_list)

my_list.append(6)
print(my_list)

new_tuple = tuple(my_list)
print(new_tuple)

# Deleting tuples
# del my_tuple1
# print(my_tuple1)
