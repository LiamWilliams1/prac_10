def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n < 0:
        print(n ** 2)
    do_something(n - 1)
print ()