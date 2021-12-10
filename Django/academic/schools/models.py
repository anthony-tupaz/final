from django.db import models
from django.db.models.fields.related import ForeignKey

class student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    created_at = models.DateTimeField(default="")
    
class subject(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    course = models.CharField(max_length=3)
    created_at = models.DateTimeField(default="")

class subject(models.Model):
    id_student = models.ForeignKey(student, null=True, blank=True, on_delete=models.CASCADE)
    id_subject = models.ForeignKey(subject, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default="")