# Key value map. Hash table. JavaScript object.
x = {
    'key': 4
}
print(x['key'])

# Adding stuff
x['nieuw'] = '🤙'
print(x)

# Check if present
print('nieuw' in x)

# All values
print(x.values())

# Loops
for key,  value in x.items():
    print(key, value)

# Delete values
del x['nieuw']
print(x)
