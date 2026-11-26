students={}
while True:
    print("A. Add a student")
    print("B. Update marks")
    print("C search for a student")
    print("D. Display all student and marks")
    print("E. Exit")

    user_input=input("Enter your choice here: ").upper()

    if user_input=="A":
        name=input("Enter your name: ")
        marks=int(input("Enter student marks: "))

        students[name]=marks

        print("Student added succesfully!!")

    elif user_input=="B":
        name=input("Enter student name here: ")

        if name in students:
            marks=int(input("Enter updated makrs here: "))
            students[name]=marks
            print("Marks added successfully!!")
        else:
            print("Student not found!!")

    elif user_input=="C":
        name=input("Enter name here: ")

        if name in students:
            print("Student is found!!")
            print("student name: ", students[name])
        else:
            print("student is not found!!")  

    
    elif user_input=="D":
            for name , marks in students.items():
                 print(name,":",marks)        

    elif user_input=="E":
         exit()
    else:
         print("invalid choice!!")  

         break             



     
  