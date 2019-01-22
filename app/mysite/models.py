from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length = 196)
    message = models.TextField()

    def __str__(self):
        return self.email
