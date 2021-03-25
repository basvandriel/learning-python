# Lambda: one line function
def x(x, y): return x + y * y


print(x)

elements = [1, 2, 3, 4, 5, 15123, 5123, 1235]

mp = map(lambda i: i * 2.2, elements)
print(list(mp))
print(mp)

mp = filter(lambda i: i % 2 == 0, elements)
print(list(mp))
