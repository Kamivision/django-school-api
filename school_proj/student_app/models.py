from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255, null = False, blank = False)
    student_email = models.EmailField(null = False, blank = False, unique=True)
    personal_email = models.EmailField(null = False, blank = False, unique=True)
    locker_number = models.IntegerField(default=1, null = False, blank = False, unique=True)
    locker_combination = models.CharField(max_length=255, null = False, blank = False, default='12-12-12')
    good_student = models.BooleanField(default=True)
    
    def __str__(self):
        return f"< {self.name} - {self.student_email} - {self.locker_number}>"
    
    def locker_assignment(self, new_locker):
        self.locker_number = new_locker
        #.save inserts or updates instance
        self.save()
    
    def student_status(self, status):
        self.good_student = status
        self.save()
            