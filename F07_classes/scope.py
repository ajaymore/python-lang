__author__ = 'Mystique'


def scope_test():
    def do_local():
        spam = "local spam"  # local scope, limited to function

    def do_nonlocal():
        nonlocal spam  # scope up to enclosing function
        spam = "nonlocal spam"

    def do_global():
        global spam  # global scope
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


scope_test()
print("In global scope:", spam)
