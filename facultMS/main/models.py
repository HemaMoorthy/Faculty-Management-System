from django.db import models

# Create your models here.


class Dept(models.Model):
    deptId=models.IntegerField()
    name=models.CharField(max_length=10)
    fname=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Subject(models.Model):
    subId=models.IntegerField()
    name=models.CharField(max_length=10)
    fname=models.CharField(max_length=100, null=True)
    dept=models.ForeignKey(Dept, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name

class Faculty(models.Model):
    facId=models.IntegerField()
    name=models.CharField(max_length=100)
    dept=models.CharField(max_length=1000, null=True)
    subjects=models.CharField(max_length=1000, null=True)
    experience=models.IntegerField()
    salary=models.FloatField()
    
    def __str__(self):
        return self.name



    