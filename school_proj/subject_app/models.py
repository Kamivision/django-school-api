from django.db import models

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(
        max_length=255, 
        null=False, 
        blank=False, 
        unique=True
        )
    
    professor = models.CharField(
        max_length=255, 
        null=False, 
        blank=False
        )
    
    # students = models.ManyToManyField(
    #     to='student_app.Student', 
    #     related_name='subjects')
    
    def __str__(self):
        return f"< {self.subject_name} >"