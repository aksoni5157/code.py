# print("hello world")

#Square star pattern
# for i in range(5): 
#     for j in range(5):
#         print("*",end=' ')
#     print()

# Right star pattern.
# for i in range(5): 
#     for j in range(i+1):
#         print('*',end=' ')
#     print()

# Right star in riverse order.
# for i in range(5,0,-1): 
#     for j in range(i):
#         print("*",end=' ')
#     print()

# for i in range(5):

#     for j in range(i):
#         print(" ",end=' ')
#         print("*",end=' ')
#     print ()

# print("hello world")

# file handling

# f=open("student.txt",'r')
# print(f.read())

# f=open("student.txt",'a')
# f.write("hello world")
# f.close()
# f=open("student.txt",'r')
# print(f.read())

# f=open("student.txt",'w')
# f.write("hello world")

# import secrets
# password=secrets.token_urlsafe(4)
# print(password)

# student detail 
# class student:

#     def __init__(self,name, roll_no,age):
#         self.name = name
#         self.roll_no = roll_no
#         self.age=age


#     def display(self):
#         print("name",self.name)
#         print("roll_no",self.roll_no)
#         print("age",self.age)

# s1=student("Akash",101,19)
# s2=student("anukaran",102,19)
# s3=student("cp",103,20)

# s1.display()
# s2.display()
# s3.display()


# class rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth

#     def area(self):
#         return self.length * self.breadth
# r1=rectangle(10,5)
# r2=rectangle(5,25)

# print("area of rectangle",r1.area())
# print("area of rectangle",r2.area())

# class movie:
#     def __init__(self,name,year):
#         self.name=name
#         self.year=year

#     def display(self):
#         print("movie name",self.name)
#         print("movie year",self.year)

# movies=[]
# n=int(input("number of movie "))
# for i in range (n):
#     name=input("movie name")
#     year=int(input("movie year"))

#     m=movie(name,year)
#     movies.append(m)
# print("\nmovie details")
# for movie in movies:
#     movie.display()
#     print()

# class student:
#     def __init__(self):
#         self.name=input("enter your name")
#         self.id=int(input("Enter your id"))
#         self.roll_no=int(input("enter roll no."))

# class examination(student):
#     def calculate(self):
#         self.maths=int(input("enter marks maths"))
#         self.physics=int(input("enter marks of physics"))
#         self.python=int(input("enter marks of python"))
#         total_marks=self.maths+self.physics+self.python
#         percentage=total_marks/3
#         print("name=",self.name)
#         print("id=",self.id)
#         print("roll_no=",self.roll_no)
#         print("maths=",self.maths)
#         print("physics=",self.physics)
#         print("python=",self.python)
#         print("total_marks",total_marks)
#         print("percentage",percentage)
# e=examination()
# e.calculate()

# class employee:
#     def info(self):
#         self.name=input("enter your name")
#         self.id=int(input("enter your id"))
#         self.salary=int(input("enter your salary"))

# class manager(employee):
#     def total(self):
#         bonous=(self.salary*10)/100
#         total_salary=bonous+self.salary
#         print("name=",self.name)
#         print("id=",self.id)
#         print("salary",self.salary)
#         print("boonous=",bonous)
#         print("total_salary=",total_salary)
# e=manager()
# e.info()
# e.total()

# class Academic:
#     def marks(self):
#         self.python=int(input("Enter python marks"))
#         self.de=int(input("Enter de marks"))
#         self.maths=int(input("Enter maths marks"))

# class sports:
#     def info(self):
#         self.sports_marks=int(input("Enter sports marks:"))
#         print()

# class result(Academic,sports):
#     def total(self):
#         print("python marks",self.python)
#         print("de marks",self.de)
#         print("maths marks",self.maths)
#         print("sports marks",self.sports_marks)
        
# e=result()
# e.marks()
# e.info()
# e.total()

# class personal_details:
#     def info(self):
#         self.name=input("enter your name: ")
#         self.age=input("enter your age:")
#         self.city=input("enter your city:")
# class professional_details:
#     def details(self):
#         self.company_name=input("Enter company name=")
#         self.designation=input("Enter your designation=")
#         self.experience=int(input("Enter your experience"))
#         print(self.experience,"years")
#         print()

# class employee(personal_details,professional_details):
#     def display(self):
#         print("name=",self.name)
#         print("age=",self.age)
#         print("city=",self.city)
#         print("company name=",self.company_name)
#         print("designation=",self.designation)
#         print("Experience=",self.experience,"years")
# a=employee()
# a.info()
# a.details()
# a.display()

# class person:
#     def __init__(self,name,age,height,weight):
#         self.name=name
#         self.age=age
#         self.height=height
#         self.weight=weight

# class student(person):
#     def __init__(self,name,age,height,weight,roll_no,marks):
#         super().__init__(name,age,height,weight)

#         self.roll_no=roll_no
#         self.marks=marks
        
#     def display(self):
#         print("name=",self.name)
#         print("age=",self.age)
#         print("height=",self.height)
#         print("weight=",self.weight)
#         print("roll_number=",self.roll_no)
#         print("marks=",self.marks)
# name=input("enter name:")
# age=int(input("enter age:"))
# height=int(input("enter height:"))
# weight=int(input("enter weight:"))
# roll_no=int(input("enter roll number:"))
# marks=int(input("enter marks:"))
# a=student(name,age,height,weight,roll_no,marks)
# a.display()

class person:
    def info(self):
        self.student_name=input("enter student name:")
        self.roll_no=int(input("enter roll_no:"))

class teacher(person):
    def display(self):
        super().info()
        self.subject=input("enter subject name:")
        self.teacher_name=input("enter teacher name:")
        print()
        print("name=",self.student_name)
        print("roll_no=",self.roll_no)
        print("subject=",self.subject)
        print("teacher name",self.teacher_name)
a=teacher()
a.display()



        



        




