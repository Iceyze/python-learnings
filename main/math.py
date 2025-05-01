import operator

def hello(a, op_str, c):
   ops = {
        "*": operator.mul,
        "+": operator.add,
        "-": operator.sub,
        "/": operator.floordiv
    }
   print(ops[op_str](a, c))

hello(69, "", 69)