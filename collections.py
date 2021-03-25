# Un- or ordered list of elements
elements = [3, 3, 3]
string = 'Hi'

e_lements = elements
bop = e_lements[:]

print(elements)
print(len(elements), len(string))

# Appending
elements.append(4)
print(elements)

# Extending
elements.extend([1, 2, 3])
print(elements)

# Remove and return last element
print(elements.pop())
print(elements.pop(1))

# Accessing collection
print(elements[0])

# Lists are mutable, reference to list
elements[0] = 'Hey'
print(elements, e_lements)

# Copy of list
print(bop)

# Tuples. Can't be changed. Only re-defined
del elements
elements = (1, 2, 3, 4)

print(elements, elements[0])
