# fruits = ["apple", "banana", "cherry"]
# print(fruits)

# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])    # First item
# print(fruits[-1])   # Last item

# fruits = ["apple", "banana"]
# fruits.append("cherry")    # Add to end
# fruits.insert(1, "mango")  # Add at position 1
# print(fruits)

# fruits = ["apple", "banana", "cherry"]
# fruits.remove("banana")    # Remove by value
# popped = fruits.pop()      # Remove last
# print(fruits)
# print("Removed:", popped)

# fruits = ["apple", "banana", "cherry"]
# fruits[1] = "mango"        # Change index 1
# print(fruits)

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

# fruits = ["apple", "banana", "cherry"]
# if "banana" in fruits:
#     print("Yes, banana is in the list")

# nums = [10, 20, 30, 40, 50]
# print(nums[0:3])   # First 3 items
# print(nums[1:4])   # Items 1 to 3
# print(nums[:2])    # First 2
# print(nums[2:])    # From index 2 to end

# nums = [5, 2, 8, 1, 9]
# nums.sort()        # Small to large
# print(nums)
# nums.reverse()     # Reverse order
# print(nums)

# fruits = ["apple", "banana", "cherry"]
# print("Length:", len(fruits))

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# combined = list1 + list2
# print(combined)

# nums = [1, 2, 3]
# repeated = nums * 3
# print(repeated)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# fruits = ["apple", "banana", "cherry"]
# print("Index of banana:", fruits.index("banana"))

# nums = [1, 2, 2, 3, 2, 4]
# print("Number of 2s:", nums.count(2))

# fruits = ["apple", "banana", "cherry"]
# fruits.clear()
# print(fruits)  # []

original = [1, 2, 3]
copy = original.copy()   # Independent copy
original.append(4)
print("Original:", original)
print("Copy:", copy)     # Copy stays same