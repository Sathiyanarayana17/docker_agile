class Student:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def display(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Course: {self.course}"