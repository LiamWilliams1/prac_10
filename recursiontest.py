def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# TODO: 1. write down what you think the output of this will be,

# TODO: 2. use the debugger to step through and see what's actually happening
print(do_it(5))