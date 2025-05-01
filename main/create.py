import random

def create(a, b):
    number = random.randint(a, b)
    if number == 1:
        print(r"""-
----
|   |
| o |
|   |
-----

    """), 
    if number == 2:
        print(r"""
-----
|o  |
|   |
|  o|
-----"""),
    if number == 3:
        print(r"""
-----
|o  |
| o |
|  o|
-----"""),
    if number == 4:
        print(r"""
-----
|o o|
|   |
|o o|
-----"""),
    if number == 5:
        print(r"""
-----
|o o|
| o |
|o o|
-----"""),
    if number == 6:
        print(r"""
-----
|o o|
|o o|
|o o|
-----"""),
    return number