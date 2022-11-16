from django.db import models

# Create your models here.
class facultyMember(models.Model):
    inputId = models.CharField(max_length = 10)
    inputName = models.CharField(max_length = 100)
    inputEmploymentStatus = models.CharField(max_length = 100)
    inputCollege = models.CharField(max_length = 100)
    inputDepartment = models.CharField(max_length = 100)
    inputExpertiseSubject = models.CharField(max_length = 300) #Checkbox 
    inputDayAvailability = models.CharField(max_length = 100) #Checkbox With InputField Below | Calendar
    inputTimePreference = models.CharField(max_length = 100) #Checkbox With InputField Below | Calendar
    inputUnitsLoad = models.CharField(max_length = 100)

    def __str__(self):
        return self.inputName
        

