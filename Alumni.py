class Alumni:
    def __init__(self, alumni_id, name, graduation_year):
        self.alumni_id = alumni_id
        self.name = name
        self.graduation_year = graduation_year

    def display(self):
        return (
            f"Alumni ID: {self.alumni_id}, "
            f"Name: {self.name}, "
            f"Graduation Year: {self.graduation_year}"
        )