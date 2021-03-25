# Simple
def func():
    print('Hey!')


def func_in_func():
    def inner():
        return '🤙'

    print(inner())


func()
func_in_func()

# Arguments


def calculate(x, y):
    return x * y


print(calculate(2, 590))


# Multiple returns
def calculate_multi(x, y):
    return x * y, x / y


result = calculate_multi(100, 120.4)
print(result)

r1, r2 = result
print(r1, r2)

# Optionals


def optional(x, y, z=None):
    print("Running", x, y, z)


optional(5, 12, 12)
