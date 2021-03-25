# Slice operator, used to take piece of collection or list. Similar to range function; start:stop:step

elements = ['Hey', 'Hi', 'Goedendag']
sliced = elements[0:2:1]

print(sliced)

sliced = elements[2:0:-1]
print(sliced)

# Reverse a list. Start at beginning, start at end and step by -1
sliced = elements[::-1]
print(sliced)

# Works on strings too
msg = 'Hey'
print(msg[::-1])

# And tuples
sliced = (1, 2, 4, 5, 6)[::-1]
print(sliced)
