from django.db import models
from ckeditor.fields import RichTextField
from datetime import date
# Create your models here.



class Notice(models.Model):
    post_id = models.AutoField(primary_key= True)
    title = models.CharField(max_length=50)
    head = models.CharField(max_length=500, default="")
    body = RichTextField(blank=False, null=True)

    pub_date = models.DateField()
    thumbnail = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

class Programs(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null= True, max_length=255)
    about = RichTextField(blank=False, null=True)
    excerpt = models.TextField(default="ABC")
    image = models.ImageField(default="")

    def __str__(self):
        return self.name

class Career(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)
    email  = models.CharField(blank=False, null=False, max_length=255)
    address = models.CharField(blank=False, null=False, max_length=255)
    contact = models.CharField(blank=False, null=False, max_length=255)
    document = models.FileField(upload_to='doc/')  

    def __str__(self):
        return self.name 


class Contact(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name



class Register(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    GRADE_CHOICES = [
        ('kindergarten','kindergarten'),
        ('nursery','nursery'),
        ('1 class','1 class'),
        ('2 class','2 class'),
        ('3 class','3 class'),
        ('4 class','4 class'),
        ('5 class','5 class'),
        ('6 class','6 class'),
        ('7 class','7 class'),
        ('8 class','8 class'),
        ('9 class','9 class'),
        ('10 class','10 class')

    ]
    student_name = models.CharField(max_length=100, blank=False, null=False,default='')
    dob = models.DateField(default=date.today)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,default='')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField(default='')
    grade = models.CharField(max_length=255, choices = GRADE_CHOICES, default='')

    def __str__(self):
        return self.student_name


class Departments(models.Model):
    title = models.CharField(blank=True, null= True, max_length=255)

class Academics(models.Model):
    department = models.ForeignKey(Departments, on_delete= models.CASCADE)
    name = models.CharField(blank=False, null=False, max_length=255)
    qualification = models.CharField(blank=False, null= False, max_length=255)
    image = models.ImageField(default="")

    def __str__(self):
        return self.name
    

