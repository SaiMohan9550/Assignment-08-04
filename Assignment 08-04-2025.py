# 1. Creating a set with five different numbers
my_set = {1, 2, 3, 4, 5}
print(my_set)

# 2. Adding and removing an element to the set
my_set.add(6)
my_set.remove(2)
print(my_set)


# 3. Checking if an element exists in the set
if 3 in my_set:
    print("Element 3 exists in the set.")
else:
    print("Element 3 does not exist in the set.")


# 4. Creating two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union = set1 | set2
print("Union:", union)
intersection = set1 & set2
print("Intersection:", intersection)
difference = set1 - set2
print("Difference:", difference)


# 5. Creating two sets
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
if set_a.issubset(set_b):
    print("set_a is a subset of set_b.")
else:
    print("set_a is not a subset of set_b.")


# 6. Given list with duplicates
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)
print(unique_set)


# 7. Creating sets representing students in two courses
course1 = {"Alice", "Bob", "Charlie"}
course2 = {"Charlie", "David", "Eve"}
common_students = course1 & course2
print("Students in both courses:", common_students)


# 8. Creating three sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {4, 5, 6, 7}
common_elements = set1 & set2 & set3
print("Common elements between three sets:", common_elements)


# 9. Using set comprehension to create a set of squares
squares_set = {x ** 2 for x in range(1, 11)}
print(squares_set)


# 10. Creating a frozenset
normal_set={1, 2, 3, 4}
frozen_set = frozenset([1, 2, 3, 4, 5])
print("Normal set:", normal_set)
print("Frozenset:", frozen_set)
