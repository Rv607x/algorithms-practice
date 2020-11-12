# Recursion is a function that calls itself to solve
# itself
""" we will use recursion to to find the nth fibonaci number
    formula for fining nth fibonacci number is Xn = Xn−1 + Xn−2

"""

def fib(n):
    """Returns the nth fibonacci number.

    """
    dict1 = {}
    if n < 0:
        print("Not a fibonacci number")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(9))
print(".................................")

# however the above method is very slow especially when n is a huge value like 30 or 50
# The computer will spend a lot of time computing it. We can use python dictionaries to make 
# it go faster 

dict1 = {0:0, 1:1}
def fib2(n):
    if n not in dict1:
        dict1[n] = fib2(n-1) + fib2(n-2)
    return dict1[n]

print("Fib2 values")
print(fib2(9))
print(fib2(15))
print(fib2(50))