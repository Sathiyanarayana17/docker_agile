class Fees:
    def __init__(self, student_id, amount):
        self.student_id = student_id
        self.amount = amount

    def pay(self, payment):
        if payment <= 0:
            raise ValueError("Payment must be greater than zero")

        self.amount -= payment

        if self.amount < 0:
            self.amount = 0

        return self.amount

    def display(self):
        return f"Student ID: {self.student_id}, Remaining Fees: {self.amount}"