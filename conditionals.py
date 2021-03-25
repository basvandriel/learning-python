# ==
# !=
# <=
# >=
# <
# >

# Case sensitive comparion, single or double quotes do not mattere
x = 'hello'
y = "hello"

print(x == y)

# Larger then?
print('a' > 'Z')

# Numbers in Python are stored in ASCII format
print(ord('a'), ord('Z'))

# Duh
print(7.0 > 6.0)

# In result
result = 6 > 12
print(result)

# Expressions work
x = 6
y = 1

result = x + 2 < y * 20
print(result)

# or and not chaining
diff_result = result or x > y
print(diff_result)

diff_result = result and not False
print(diff_result)

# Order of operations: not -> and -> or
