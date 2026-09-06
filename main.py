import argparse
from student import Student
from manager import StudentManager


def get_arguments():
    parser = argparse.ArgumentParser(description="Student Record Management System")

    parser.add_argument("--file", required=True)
    parser.add_argument("--format", required=True, choices=["txt", "csv", "json"])
    parser.add_argument(
        "--mode",
        required=True,
        choices=[
            "display",
            "add",
            "search-id",
            "search-name",
            "search-department",
            "search-average",
            "update",
            "remove"
        ]
    )

    parser.add_argument("--id", type=int)
    parser.add_argument("--name")
    parser.add_argument("--department")
    parser.add_argument("--semester", type=int)
    parser.add_argument("--dbms", type=float)
    parser.add_argument("--os", type=float)
    parser.add_argument("--computer-network", type=float)
    parser.add_argument("--average", type=float)

    return parser.parse_args()


def display_results(students):
    if len(students) == 0:
        print("No matching students found.")
        return

    for student in students:
        student.display_student()


def add_student(manager, args):
    if (
        args.id is None or
        args.name is None or
        args.department is None or
        args.semester is None or
        args.dbms is None or
        args.os is None or
        args.computer_network is None
    ):
        print("All student details are required.")
        return

    student = Student(
        args.id,
        args.name,
        args.department,
        args.semester,
        args.dbms,
        args.os,
        args.computer_network
    )

    manager.add_student(student)
    manager.save_to_file(args.file, args.format)

    print("Student added successfully.")


def search_student_by_id(manager, student_id):
    student = manager.search_student(student_id)

    if student is None:
        print("Student not found.")
    else:
        student.display_student()


def update_student(manager, args):
    student = manager.search_student(args.id)

    if student is None:
        print("Student not found.")
        return

    if (
        args.dbms is None or
        args.os is None or
        args.computer_network is None
    ):
        print("All three subject marks are required.")
        return

    student.update_marks(
        args.dbms,
        args.os,
        args.computer_network
    )

    manager.save_to_file(args.file, args.format)

    print("Student marks updated successfully.")


def main():
    args = get_arguments()

    manager = StudentManager()

    manager.load_from_file(args.file, args.format)

    if args.mode == "display":
        manager.display_all_students()

    elif args.mode == "add":
        add_student(manager, args)

    elif args.mode == "search-id":
        if args.id is None:
            print("Student ID is required.")
        else:
            search_student_by_id(manager, args.id)

    elif args.mode == "search-name":
        if args.name is None:
            print("Name is required.")
        else:
            students = manager.search_by_name(args.name)
            display_results(students)

    elif args.mode == "search-department":
        if args.department is None:
            print("Department is required.")
        else:
            students = manager.search_by_department(args.department)
            display_results(students)

    elif args.mode == "search-average":
        if args.average is None:
            print("Average value is required.")
        else:
            students = manager.search_by_average(args.average)
            display_results(students)

    elif args.mode == "update":
        if args.id is None:
            print("Student ID is required.")
        else:
            update_student(manager, args)

    elif args.mode == "remove":
        if args.id is None:
            print("Student ID is required.")
        else:
            removed = manager.remove_student(args.id)

            if removed:
                manager.save_to_file(args.file, args.format)
                print("Student removed successfully.")
            else:
                print("Student not found.")


if __name__ == "__main__":
    main()

