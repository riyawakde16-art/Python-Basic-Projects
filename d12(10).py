import math, random
from datetime import datetime
history = {}
last = None
def basic():
    try:
        a = float(input("First: "))
        op = input("Operator (+,-,*,/): ")
        b = float(input("Second: "))
        if op == "+": return a + b
        elif op == "-": return a - b
        elif op == "*": return a * b
        elif op == "/": return a / b
        else: print("Invalid operator")
    except Exception:
        print("Error:")
while True:
    print("\n1.Basic ")
    print("2.Scientific")
    print("3.Random ")
    print("4.Store ")
    print("5.History")
    print("6.Exit")
    ch = input("Choice: ")
    if ch == "1":
        last = basic()
        print("Result:", last)
    elif ch == "2":
        x = float(input("Enter number: "))
        last = math.sqrt(x)
        print("Square Root:", last)
    elif ch == "3":
        last = random.randint(1, 100)
        print("Random Number:", last)
    elif ch == "4":
        if last is not None:
            history[datetime.now().strftime("%H:%M:%S")] = last
            print("Stored!")
    elif ch == "5":
        for t, r in history.items():
            print(t, ":", r)
    elif ch == "6":
        print("Exit")
        break
    else:
        print("Invalid Choice")