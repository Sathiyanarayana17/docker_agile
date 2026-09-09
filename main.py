from Student import Student
from Faculty import Faculty
from Course import Course
from Fees import Fees
from Alumni import Alumni


def main():
    print("================================")
    print(" Student Management System")
    print("================================")

    student = Student(101, "Arun", "Computer Science")
    faculty = Faculty(201, "Dr. Kumar", "Computer Science")
    course = Course(301, "Python Programming", "3 Months")
    fees = Fees(101, 50000)
    alumni = Alumni(401, "Rahul", 2024)

    print(student.display())
    print(faculty.display())
    print(course.display())
    print(fees.display())

    remaining = fees.pay(10000)
    print(f"After payment, remaining fees: {remaining}")

    print(alumni.display())
    print("\nApplication executed successfully!")


if __name__ == "__main__":
    main()