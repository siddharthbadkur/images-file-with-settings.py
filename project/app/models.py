from django.db import models

# Create your models here.
class Studentmodel(models.Model):
    stu_name=models.CharField(max_length=100)
    stu_image=models.ImageField(upload_to='image/')
    stu_resume=models.FileField(upload_to='Files/')
