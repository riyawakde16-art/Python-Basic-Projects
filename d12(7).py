square = lambda a: a * a
try:
    n = list(range(1, 21))
    s = list(map(square, n))
    even_squ = [x for x in s if x % 2 == 0]
    print("Squares:", s)
    print("Even Squares:", even_squ)
except Exception:
    print("Error:")