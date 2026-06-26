import math
try:
    s = input("Enter a sentence: ")
    w = s.split()
    unique_words = set(w)
    print("Unique words (sorted):")
    for w in sorted(unique_words):
        print(w)
    total_unique = len(unique_words)
    r = math.pow(total_unique, 2)
    print("Total unique words:", total_unique)
    print("Square:", r)
except Exception:
    print("Error!")