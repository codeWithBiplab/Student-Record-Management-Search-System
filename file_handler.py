import csv
import json
from student import Student


class FileHandler:

    @staticmethod
    def read_txt(filename):
        students = []

        with open(filename, "r") as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()

            if line:
                data = line.split(",")

                student = Student(
                    data[0].strip(),
                    data[1].strip(),
                    data[2].strip(),
                    data[3].strip(),
                    data[4].strip(),
                    data[5].strip(),
                    data[6].strip()
                )

                students.append(student)

        return students

    @staticmethod
    def write_txt(filename, students):
        with open(filename, "w") as file:
            for student in students:
                line = (
                    str(student.student_id) + ", " +
                    student.name + ", " +
                    student.department + ", " +
                    str(student.semester) + ", " +
                    str(student.dbms) + ", " +
                    str(student.os) + ", " +
                    str(student.computer_network) + "\n"
                )

                file.write(line)

    @staticmethod
    def read_csv(filename):
        students = []

        with open(filename, "r") as file:
            reader = csv.reader(file)

            next(reader)

            for row in reader:
                if row:
                    student = Student(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6]
                    )

                    students.append(student)

        return students

    @staticmethod
    def write_csv(filename, students):
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Student_ID",
                "Name",
                "Department",
                "Semester",
                "DBMS",
                "OS",
                "Computer_Network"
            ])

            for student in students:
                writer.writerow([
                    student.student_id,
                    student.name,
                    student.department,
                    student.semester,
                    student.dbms,
                    student.os,
                    student.computer_network
                ])

    @staticmethod
    def read_json(filename):
        students = []

        with open(filename, "r") as file:
            data = json.load(file)

        for item in data:
            marks = item["marks"]

            student = Student(
                item["student_id"],
                item["name"],
                item["department"],
                item["semester"],
                marks["dbms"],
                marks["os"],
                marks["computer_network"]
            )

            students.append(student)

        return students

    @staticmethod
    def write_json(filename, students):
        data = []

        for student in students:
            item = {
                "student_id": student.student_id,
                "name": student.name,
                "department": student.department,
                "semester": student.semester,
                "marks": {
                    "dbms": student.dbms,
                    "os": student.os,
                    "computer_network": student.computer_network
                }
            }

            data.append(item)

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

