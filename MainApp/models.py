from django.db import models

# Create your models here.
class facultyMember(models.Model):
    inputId = models.CharField(max_length = 10)
    inputName = models.CharField(max_length = 100)
    inputContactNumber = models.CharField(max_length = 11)

    def __str__(self):
        return self.inputName
        

