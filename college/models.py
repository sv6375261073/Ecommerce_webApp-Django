from django.db import models
class Teacher(models.Model):
    id=models.AutoField
    Name=models.CharField(max_length=20)
    Address=models.CharField(max_length=30)
    Salary=models.IntegerField()
    image = models.ImageField(upload_to="college/images/", default="")
    def __str__(self):
        return self.Name

class Student(models.Model):
    Id=models.AutoField
    Name=models.CharField(max_length=30)
    desc=models.CharField(max_length=20,default='Playboy')
    college=models.CharField(max_length=10,default='RIET')
    DOB=models.DateField()
    image=models.ImageField(upload_to="college/images/",default="")

    def __str__(self):
        return self.Name
