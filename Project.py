class Student :

    def __init__(self, student_id, name, department):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = False


    def get_id (self):
        return self.__student_id
    
    def get_name (self):
        return self.__name
    
    def get_dept (self):
        return self.__department
    
    def get_status (self):
        return self.__is_enrolled 


    def enroll_student(self):

        if self.__is_enrolled:
            print(f"\n\t---> FAHHHHHH: {self.__student_id} is already enrolled!!!")
        
        else :
            self.__is_enrolled = True
            print(f"\n\t---> Wow: {self.__name} with id {self.__student_id} is enrolled successfully.")


    def drop_student (self):

        if not self.__is_enrolled:
            print(f"\n\t---> FAHHHHHH: {self.__student_id} is not enrolled yet!!!")

        else:
            self.__is_enrolled = False
            print(f"\n\t---> Wow: {self.__name} with id {self.__student_id} is dropped successfully.")


    def view_student_info (self):

        status = "Enrolled"
        if not self.__is_enrolled:
            status = "Not enrolled"

        print(f"\t{self.__student_id}\t{self.__name}\t\t{self.__department}\t\t{status}")



class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, st_obj):
        cls.student_list.append(st_obj)
        print(f"ID: {st_obj.get_id()} Student: {st_obj.get_name()} added to database.")


s1 = Student(101, "Sayem", "CSE")
StudentDatabase.add_student(s1)

s2 = Student(102, "Hasib", "SWE")
StudentDatabase.add_student(s2)

s3 = Student(103, "Adu Vai", "BBA")
StudentDatabase.add_student(s3)

s4 = Student(104, "Jahid", "IPE")
StudentDatabase.add_student(s4)

while True:
    print("\n------------------------------------")
    print("\tStudent Management System")
    print("------------------------------------")
    
    print("Options:\n")
    print("1: View All Students")
    print("2: Enroll Student")
    print("3: Drop Student")
    print("4: Exit")

    ch = int(input("\nEnter Option: "))
        
    if ch < 1 or ch > 4:
        print("\n\t---> !!! Please enter a valid number")
        continue

    if ch == 1:
        print("\n\t--- All Students ---\n")
        print(f'\tID\tName\t\tDept\t\tStatus')
        print("\t----------------------------------------------")
        for student in StudentDatabase.student_list:
            student.view_student_info()

    elif ch == 2:
        print("\tEnter student id you want to enroll: ")
        student_id = int(input())
        found = False
        for student in StudentDatabase.student_list:
            if student.get_id() == student_id:
                student.enroll_student()
                found = True
                break
        if not found:
            print(f"\n\t---> FAHHHHHH: Student with ID {student_id} not found in the database!")

    elif ch == 3:
        print("\tEnter student id you want to drop: ")
        student_id = int(input())
        found = False
        for student in StudentDatabase.student_list:
            if student.get_id() == student_id:
                student.drop_student()
                found = True
                break
        if not found:
            print(f"\n\t---> FAHHHHHH: Student with ID {student_id} not found in the database!")


    elif ch == 4:
        print("\nExiting System... Goodbye!")
        break

    else:
        print("\n\t---> !!! Choose a Valid Option between (1 - 4)\n")