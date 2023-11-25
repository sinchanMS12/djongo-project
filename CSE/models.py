# students/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    departent = models.CharField(max_length=10)
    rollnumber = models.IntegerField()
    # cgpa=models.IntegerField()
    def _str_(self):
        return self.name





class Class1(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student1(models.Model):
    first_name = models.CharField(max_length=30, default="ram")
    last_name = models.CharField(max_length=30, default='kumar')
    email = models.EmailField(unique=True, default='ram@gmail.com')
    date_of_birth = models.DateField()
    usn = models.CharField(max_length=20, unique=True)  # Assuming USN is a string of max length 20
    department = models.CharField(max_length=50)
    cgpa = models.DecimalField(max_digits=3, decimal_places=2)  # Assuming CGPA is stored as a decimal
    total_marks = models.IntegerField()
    student_class = models.ForeignKey(Class1, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.usn}"
