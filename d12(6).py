import random
import math
n = set()
try:
    for i in range(10):
        num = float(input("Enter number: "))
        n.add(num)
    print("Unique numbers (set):", n)
    num_tuple = tuple(n)
    print("Tuple:", num_tuple)
    if len(num_tuple) >= 3:
        print("Random 3 numbers:", random.sample(num_tuple, 3))
    else:
        print("Not enough elements for random selection")
    total = sum(num_tuple)
    print("Square root of sum:", math.sqrt(total))
except ValueError:
    print("Invalid input!")