from django.db import models

# Create your models here.
class facultyMember(models.Model):
    inputId = models.CharField(max_length = 10)
    inputName = models.CharField(max_length = 100)
    inputDepartment = models.CharField(max_length = 100) #Choicefield
    inputEmploymentStatus = models.CharField(max_length = 100) #Choicefield
    inputExpertiseSubject = models.CharField(max_length = 100) #Checkbox
    inputDayAvailability = models.CharField(max_length = 100) #Checkbox
    inputTimePreference = models.CharField(max_length = 100) #Choicefield
    inputUnitsLoad = models.CharField(max_length = 100)

    def __str__(self):
        return self.inputName
        

