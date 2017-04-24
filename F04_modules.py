__author__ = 'Mystique'

import sys

print(sys.path)
print(dir())

from import_me_parent import fib

fib(100)

import sub_package.import_me
import import_me_parent
from sub_package2.import_me import print_hello

sub_package.import_me.print_hello()
print_hello()
print(import_me_parent.__author__)