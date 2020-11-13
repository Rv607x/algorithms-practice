# Euclidean Algorithm is A special way to find the greatest common factor of two integers.

# With the larger number in 1st spot:
# • divide the 1st number by the 2nd number. Note down the remainder.
# • move the 2nd number into 1st spot, and put the remainder from the previous step in 2nd spot
# • repeat until the remainder is zero




def gcd(a, b):
    if a % b == 0:
        return b
    else:
        x = b
        y = a % b
        return gcd(x, y)

print(gcd(112, 42))    
print(gcd(100, 40))   
print(gcd(16457, 1638))
print(gcd(1680, 640))
print(gcd(420,69))