class Student:
    def __init__(self, student_id, name, department, semester, dbms, os, computer_network):
        self.student_id = int(student_id)
        self.name = name
        self.department = department
        self.semester = int(semester)
        self.dbms = float(dbms)
        self.os = float(os)
        self.computer_network = float(computer_network)

    def calculate_total(self):
        return self.dbms + self.os + self.computer_network

    def calculate_average(self):
        return self.calculate_total() / 3

    def get_result(self):
        if self.dbms >= 40 and self.os >= 40 and self.computer_network >= 40:
            return "Pass"
        return "Fail"

    def update_marks(self, dbms, os, computer_network):
        self.dbms = float(dbms)
        self.os = float(os)
        self.computer_network = float(computer_network)

    def display_student(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Semester:", self.semester)
        print("DBMS:", self.dbms)
        print("OS:", self.os)
        print("Computer Network:", self.computer_network)
        print("Total Marks:", self.calculate_total())
        print("Average Marks:", round(self.calculate_average(), 2))
        print("Result:", self.get_result())
        print()

