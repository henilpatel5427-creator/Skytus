# 1. Create a tuple with 5 numbers
print("1:")

numbers = (10, 20, 30, 40, 50)

# 2. Access the third element in a tuple (index starts at 0)
print("2:")

third_element = numbers[2]
print("Third element:", third_element)

# 3. Unpack a tuple into separate variables
print("3:")

a, b, c, d, e = numbers
print("Unpacked values:", a, b, c, d, e)

# 4. Create a set of 5 fruits
print("4:")

fruits = {"apple", "banana", "orange", "mango", "grape"}

# 5. Add a new fruit to the set
print("5:")
fruits.add("pineapple")
print("After adding:", fruits)

# 6. Remove an element from a set
print("6:")

fruits.remove("banana")
print("After removing:", fruits)

# 7. Find union of two sets
print("7:")

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union_set = set1.union(set2)
print("Union:", union_set)

# 8. Find intersection of two sets
print("8:")

intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# 9. Check if one set is subset of another
print("9:")

subset_check = {1, 2}.issubset(set1)
print("Is subset:", subset_check)

# 10. Convert a list with duplicate values into a set to remove duplicates
print("10:")

list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(list_with_duplicates)
print("Set without duplicates:", unique_set)



# python data strutures:-


# Create a dictionary storing student names and marks.
print("11:")
students = {"henil": 80, "darshil": 75, "aryan": 90}
print(students)

# Add a new key-value pair to an existing dictionary.
print("12:")

students["aryan"] = 85
print(students)

# Delete a key-value pair from a dictionary.
print("13:")

del students["darshil"]
print(students)

# Merge two dictionaries into one.
print("14:")

d1 = {"A": 10, "B": 20}
d2 = {"C": 30, "D": 40}

d3 = d1 | d2
print(d3)

# Check if a key exists in a dictionary.
print("15:")

if "henil" in students:
    print("Key exists")
else:
    print("Key does not exist")

# Count word frequency in a given string using a dictionary.
print("16:")

text = "cat dog cat bird dog cat"
words = text.split()

count = {}

for w in words:
    count[w] = count.get(w, 0) + 1

print(count)

# Find the key with the maximum value in a dictionary.
print("17:")

marks = {"henil": 80, "darshil": 75, "aryan": 90}

topper = max(marks, key=marks.get)
print(topper)

# Reverse keys and values in a dictionary.
print("18:")

data = {"a": 1, "b": 2, "c": 3}

reverse = {v: k for k, v in data.items()}
print(reverse)

# Update the value for a specific key.
print("19:")

students["henil"] = 95
print(students)

# Convert a list of tuples into a dictionary
print("20:")

lst = [("x", 1), ("y", 2), ("z", 3)]

result = dict(lst)
print(result)
