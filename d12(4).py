class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.rollno=roll_no
        self.marks_list=[]
        
    def add_mark(self,mark):
            if mark >= 0 or mark <= 100:
                 self.marks_list.append(mark)
            else:
                 print("Invalid marks!")
    def get_average(self):
         if len(self.marks_list)==0:
              return 0
         return sum(self.marks_list)/len(self.marks_list)
    def display_info(self):
         print("Name:",self.name)
         print("Roll no:",self.rollno)
         print("Marks:",self.marks_list)
         print("Average:",self.get_average())
name=input("Enter name:")
roll=input("Enter roll number:")
s= Student(name,roll)
for i in range(5):
    try:
         m=float(input("Enter marks:"))
         s.add_mark(m)
    except ValueError:
              print("Invalid input!")
s.display_info()








         


                 

