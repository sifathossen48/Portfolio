from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=50)
    profile = models.ImageField(upload_to='profile/')
    title = models.CharField(max_length=25)
    title2 = models.CharField(max_length=25)
    facebook = models.CharField(max_length=30)
    github = models.CharField(max_length=30)
    twitter = models.CharField(max_length=30)
    dribble = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=20)
    cv = models.FileField(upload_to='cv/', validators=[FileExtensionValidator(['pdf'])])

    def __str__(self):
        return self.name


class About(models.Model):
    desc = models.TextField(null=True,blank=True)
    resume_title = models.CharField(max_length=150)
    contact_title = models.CharField(max_length=150)
    contact_desc = models.TextField(null=True,blank=True)
    project_title = models.CharField(max_length=150)

    def __str__(self):
        return self.desc

class Client(models.Model):
    company = models.CharField(max_length=20)
    company_link = models.CharField(max_length=100)
    def __str__(self):
        return self.company

class Project(models.Model):
    project_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='projects/')
    project_link = models.CharField(max_length=70)
    project_desc = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.project_name

class Experience(models.Model):
    title = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
    timeline = models.CharField(max_length=30)
    desc = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title

class Education(models.Model):
    title = models.CharField(max_length=40)
    degree = models.CharField(max_length=40)
    timeline = models.CharField(max_length=30)
    desc = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.degree

class Skill(models.Model):
    name = models.CharField(max_length=20)
    percentage = models.CharField(max_length=5)
    def __str__(self):
        return self.name

class Testimonial(models.Model):
    author_name = models.CharField(max_length=30)
    author_company = models.CharField(max_length=30)
    author_image = models.ImageField(upload_to='testimonial/')
    desc = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.author_name

class Copyright(models.Model):
    site_name = models.CharField(max_length=20)
    year = models.IntegerField(max_length=5)
    designer_name = models.CharField(max_length=20)
    designer_profile_link = models.CharField(max_length=50)
    def __str__(self):
        return self.designer_name









    