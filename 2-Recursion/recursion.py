# Recursion is a function that calls itself to solve
# itself
""" we will use recursion to to find the nth fibonaci number
    formula for fining nth fibonacci number is Xn = Xn−1 + Xn−2

"""

def fib(n):
    """Returns the nth fibonacci number.

    """
    if n < 0:
        print("Not a fibonacci number")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(9))