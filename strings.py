msg = 'hello'
print(type(msg))

# Methods on string
print(msg.upper())
print(msg.lower())
print(msg.capitalize())

# Count characters, case sensitive
print(msg.count('l'))

# Nope
print(msg.upper().count('l'))

# String multiplication
x = 'Hey'
y = 3

print(x * y)

# String concatenation
y = ' nee'

print(x + y)
