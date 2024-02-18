from django.db import models

class Subjects_Model(models.Model):
    subjects_name = models.CharField(max_length=50)
    subjects_code = models.IntegerField()
    subjects_credit = models.IntegerField()

    def __str__(self):
        return self.subjects_name


class Student_Model(models.Model):
    Gender = {
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    }
    Name = models.CharField(max_length=30, null=True)
    Age = models.FloatField()
    Department = models.CharField(max_length=30, null=True)
    gender = models.CharField(choices=Gender, max_length=30, null = True)
    Subjects = models.ManyToManyField(Subjects_Model)

    def __str__(self):
        return self.Name

 
class Grade_model(models.Model):
    student = models.ForeignKey(Student_Model, on_delete = models.CASCADE, null = True)
    student_sub = models.ForeignKey(Subjects_Model, on_delete = models.CASCADE, null = True)
    marks = models.IntegerField()
    
  