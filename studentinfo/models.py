from django.db import models

# Create your models here.

class Studentdetails(models.Model):
    studentid = models.IntegerField()
    firstname = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    major = models.CharField(max_length=500)
    year = models.CharField(max_length=500)
    gpa = models.FloatField()

class Coursedetails(models.Model):
    courseid = models.IntegerField()
    coursetitle = models.CharField(max_length=500)
    coursename = models.CharField(max_length=500)
    coursesectioncode = models.IntegerField()
    coursedepartment = models.CharField(max_length=500)
    instructorfullname = models.CharField(max_length=500)

class Enrollmentdetails(models.Model):
    studentid = models.IntegerField()
    courseid = models.IntegerField()
