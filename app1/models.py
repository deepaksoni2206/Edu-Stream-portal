from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    COURSE_CHOICES = (
        ('python', 'Python'),   
        ('django', 'Django'),
        ('react', 'React'),
        ('javescript', 'JavaScript'),   
        ('java', 'Java'),
        ('c++', 'C++'),
    )
    course = models.CharField(max_length=100, choices=COURSE_CHOICES)
    price = models.FloatField()
    date = models.DateField()   

