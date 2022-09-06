#!/usr/bin/python3
if _name_ == "_main_":
    from add_0 import add
    add_0.add(1, 2)

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b))
