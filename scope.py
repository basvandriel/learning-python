name = 'bas'


def func(new):
    global name  # Don't
    name = new


print(name)
func('Klaasjan')
print(name)

raise Exception('That\'s bad')
