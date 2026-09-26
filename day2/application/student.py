class Student:
    """Represent a student."""

    def __init__(
        self,
        name,
        age,
        python,
        mathematics,
        communication,
    ):
        self.name = name
        self.age = age
        self.python = python
        self.mathematics = mathematics
        self.communication = communication

    def calculate_percentage(self):
        """Calculate the student's percentage."""
        """This function depicts the 
        
        total = self.python + self.mathematics + self.communication

        return total / 3

    def display(self):
        """Display the student's details."""
        print("Name:", self.name)
        print("Age:", self.age)
        print("Python:", self.python)
        print("Mathematics:", self.mathematics)
        print("Communication:", self.communication)
        print("Percentage:", self.calculate_percentage())
        print("Grade:", self.calculate_grade())


    def calculate_grade(self):
        percentage = self.calculate_percentage()
        if percentage >= 80:
             grade = "A"
        elif percentage >= 60:
             grade = "B"
        elif percentage >= 40:
             grade = "C"
        else:
            grade = "D"

        return grade


if __name__ == "__main__":
    student_obj1 = Student("harry",95,97,84,71)
    student_obj1.display()
    student_obj2 = Student("ram",82,76,89,91)
    student_obj2.display()
    student_obj3 = Student("riya",81,71,92,76)
    student_obj3.display()
    student_obj4 = Student("reena",91,81,71,62)
    student_obj4.display()
    student_obj5 = Student("apeksha",92,82,63,73)
    student_obj5.display()
        
