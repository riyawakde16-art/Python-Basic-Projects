def analyze_string(s):
    if s == "":
        print("Empty string entered!")
        return
    
    #Prints its length using len()
    print("Length of string:",len(s))

    #Prints the string in reverse using slicing
    print("String in reverse order:",s[::-1])

    #Counts and prints how many vowels (a,e,i,o,u) are in the string
    vowels=0
    for char in s:
        if char in "aeiouAEIOU":
          vowels += 1
    print("Number of vowels:",vowels)

  #Uses a for loop with range() to print each character with its positive and negative index.
    for i in range(len(s)):
        print(s[i],"Positive:",i,"Negative:",i-len(s))

   #Call this function with user input and handle empty string case.
a=input("Enter a string:")
analyze_string(a)