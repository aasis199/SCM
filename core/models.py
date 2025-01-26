from django.db import models
from ckeditor.fields import RichTextField

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



class Career(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)
    email  = models.CharField(blank=False, null=False, max_length=255)
    address = models.CharField(blank=False, null=False, max_length=255)
    contact = models.CharField(blank=False, null=False, max_length=255)
    document = models.FileField(upload_to='doc/')  

    def __str__(self):
        return self.name 


class Contact(models.Model):
    Name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email



class Register(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    email = models.EmailField()
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=255)
    query = models.TextField()

    def __str__(self):
        return self.email


class Departments(models.Model):
    title = models.CharField(blank=True, null= True, max_length=255)

class Academics(models.Model):
    department = models.ForeignKey(Departments, on_delete= models.CASCADE)
    name = models.CharField(blank=False, null=False, max_length=255)
    qualification = models.CharField(blank=False, null= False, max_length=255)


    def __str__(self):
        return self.name + self.department
    

