from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    Project_Id = models.CharField(max_length=100)
    Title = models.CharField(max_length=150)
    Description = models.TextField()
    Ratings = models.FloatField()
    Techstack = models.TextField()
    Owner = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.Title

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    
    #   Profile Info
    Profile_photo = models.ImageField(upload_to="images/",null=True,blank=True)
    Gender = models.CharField(max_length=10,default="male")
    Domain = models.CharField(max_length=200,default="Developer")
    Clg_Org = models.CharField(max_length=200,null=True,blank=True)
    Year = models.IntegerField(null=True,blank=True)
    # Cgpa = models.IntegerField(null=True,blank=True)
    Branch_Dept = models.CharField(max_length=100)
    Working_status = models.BooleanField(default=True)

    #   Projects and Achievements
    # Alter achievements and Skills in jsonformat 
    Skills = models.JSONField(null=True,blank=True)
    Achivements = models.JSONField(null=True,blank=True)
    Projects = models.ManyToManyField(Project) # null or blank field will not affect many to many field

    #  Contacts
    Email = models.EmailField()
    Linkedin = models.URLField()
    Mobile = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.user.username

# Check it once ig its perfect 
class Connection(models.Model):
    Sender = models.ForeignKey(Profile,related_name='Sender',on_delete=models.CASCADE) # one profile can have many connections 
    Reciever = models.ForeignKey(Profile,related_name='Reciever',on_delete=models.CASCADE) 
    Acceptance = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.Sender.user.username + " - " + self.Reciever.user.username + " [ " + str(self.Acceptance) + " ] "