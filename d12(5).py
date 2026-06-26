def student_database():
    students = {}  
    while True:
        print("\n1.Add")
        print("2.Search")
        print("3.Display")
        print("4.Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            try:
                r = input("Enter Roll No: ")
                n = input("Enter Name: ")
                a = int(input("Enter Age: "))
                c = input("Enter City: ")
                students[r] = {"name": n, "age": a, "city": c}
            except ValueError:
                print("Invalid input!")
        elif choice == "2":
            r = input("Enter Roll No to search: ")
            student = students.get(r)
            if student:
                print("Details:", student)
            else:
                print("Student not found!")
        elif choice == "3":
            for r, data in students.items():
                print("Roll: {r}, Info: {data}")
        elif choice == "4":
            print("Exit")
            break
        else:
            print("Invalid choice!")
student_database()