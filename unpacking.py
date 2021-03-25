def func(x):
    def func2():
        print(x)

    return func2


# Returns function
print(func(3))

# Calling it
print(func(3)())

# Like
x = func(3)
x()


def stars(*args, **kwargs):
    print(args, kwargs)
    pass


# Unpacking list/collection/tuple etc
x = [1, 2, 5]
print(*x)


def example(x, y):
    print(x, y)


pairs = [(1, 2), (3, 4)]

for pair in pairs:
    example(*pair)

# kwargs == keyword arguments

stars(12, 23, 4, 5, 6, one=123, two=421)
