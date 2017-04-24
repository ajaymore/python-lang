__author__ = 'Mystique'

# If ElseIF
# x = int(input("Please enter an integer: "))
x = 10
if x < 0:
    print('Negative number entered.')
elif x == 0:
    print('Zero entered.')
elif x == 1:
    print('Single entered.')
else:
    print('More entered.')

# for loop
words = ['cat', 'window', 'mouse', 'dog', 'chicken', 'man', 'kitten']
for w in words:
    print(w, len(w))

for i in range(5):
    print(i)

for i in range(0, len(words), 2):
    print(i, words[i])

# break, continue, else
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x);
            break
    else:
        print(n, 'is a prime number')

for n in range(2, 10):
    if n % 2 == 0:
        print(n, 'is even number')
        continue
    print(n, 'is odd number')

# pass statement
def initlog(*args):
    pass  # Remember to implement this.


# functions
def fib(num):
    a, b, result = 1, 2, []
    while a < num:
        print(a, end=' ')
        result.append(a)
        a, b = b, a + b
    print()  # Empty line
    return result


print(fib(100))


# argument passing
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)  # 1 positional argument
parrot(voltage=1000)  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')  # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)  # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')  # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
l = ["four million", "bleedin' demised"]
d = {"action": "VOOOOOOOOOOM", "type": "Norwegian green"}
parrot(*l, **d)


# document strings
def my_function():
    """Do nothing but document it.

        No, really it doesn't do anything.
    """
    pass


print(my_function.__doc__)