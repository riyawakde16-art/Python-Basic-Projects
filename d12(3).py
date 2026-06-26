def manage_marks():
    list=[]
    for i in range(5):
        while True:
            try:
                l=float(input("Enter marks for subject:"))
                list.append(l)
                break
            except ValueError:
              print("Invalid input!")
        
    a=sum(list)/len(list)
    h=max(list)
    l=min(list)
    list.sort(reverse = True)
    print("Marks list:",list)
    print("Average:",a)
    print("Higest:",h)
    print("Lowest:",l)
manage_marks()

