a=input("Enter a string:")
count=0
for ch in a:
    if ch in "aeiouAEIOU":
        count += 1
print("Vowels:",count)