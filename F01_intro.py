__author__ = 'Mystique'

# Variable init
myInt, myFloat, my_str_val, my_raw_str_val = 1, 2.9, 'Ajay', r'\nRwa'

# string
multiLineVar = """\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
"""
strVal = 'AjayMore'

print(multiLineVar)
print('0' * 2 + '7')
print(strVal[4])
print(strVal[0:4])
print(strVal[-1])
print(strVal[:4])
print(strVal[4:])
print(len(multiLineVar))

# Lists
squares = [1, 4, 9, 16, 25]
print(squares[:-1])
squares += [36, 49, 56]
squares.append(63)
print(squares)

# Fibonacci series
a, b = 0, 1
while b < 10:
    print(b, end=', ')
    a, b = b, a + b