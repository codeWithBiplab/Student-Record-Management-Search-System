from file_handler import FileHandler


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                return True

        return False

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student

        return None

    def search_by_name(self, name):
        result = []

        for student in self.students:
            if name.lower() in student.name.lower():
                result.append(student)

        return result

    def search_by_department(self, department):
        result = []

        for student in self.students:
            if department.lower() == student.department.lower():
                result.append(student)

        return result

    def search_by_average(self, average):
        result = []

        for student in self.students:
            if student.calculate_average() > average:
                result.append(student)

        return result

    def display_all_students(self):
        if len(self.students) == 0:
            print("No student records found.")
            return

        for student in self.students:
            student.display_student()

    def save_to_file(self, filename, file_format):
        if file_format == "txt":
            FileHandler.write_txt(filename, self.students)

        elif file_format == "csv":
            FileHandler.write_csv(filename, self.students)

        elif file_format == "json":
            FileHandler.write_json(filename, self.students)

    def load_from_file(self, filename, file_format):
        if file_format == "txt":
            self.students = FileHandler.read_txt(filename)

        elif file_format == "csv":
            self.students = FileHandler.read_csv(filename)

        elif file_format == "json":
            self.students = FileHandler.read_json(filename)

