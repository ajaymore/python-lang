__author__ = 'Mystique'

import sys

# Exceptions
try:
    f = open('myfile.txt')
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
else:
    print(f.read())
    f.close()


# Raise Exceptions
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))  # the exception instance
    print(inst.args)  # arguments stored in .args
    print(inst)  # __str__ allows args to be printed directly,
    # but may be overridden in exception subclasses
    x, y = inst.args  # unpack args
    print('x =', x)
    print('y =', y)


def zero_fails():
    x = 1 / 0


try:
    zero_fails()
except ZeroDivisionError as err:
    print('Handling run time error:', err)

# User defined
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise MyError(2 * 2)
except MyError as e:
    print('My Exception occurred, value:', e.value)
finally:
    print('Goodbye world..')