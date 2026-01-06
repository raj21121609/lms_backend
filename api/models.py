from django.db import models
from django.contrib.auth.models import User

class Tutor(models.Model):
    LANGUAGES = [
        ('EN','ENGLISH'),
        ('SP','SPANISH'),
        ('IT','ITALIAN'),
        ('GR','GERMAN'),
        ('FR','FRENCH')
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    headline = models.CharField(max_length=30,blank=True)
    tutor_description = models.CharField(max_length=2,choices= LANGUAGES)
    profile_pic = models.ImageField(upload_to='pp')
    #links 
    website = models.URLField(null=True,blank=True)
    x = models.URLField(null=True,blank=True)
    linkdin = models.URLField(null=True,blank=True)
    youtube = models.URLField(null=True,blank=True)
    facebook = models.URLField(null=True,blank=True)
class Comments(models.Model):
    STAR_NO = [
        ('1','ONE'),
        ('2','TWO'),
        ('3','THREE'),
        ('4','FOUR'),
        ('5','FIVE')
    ]
    student_user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    stars = models.CharField(choices=STAR_NO)
    date = models.DateField( auto_now_add=True)
class Courses(models.Model):
    NOTES_TYPES = [
        ('PD','PDF'),
        ('PT','PPT')
    ]
    price = models.IntegerField()
    title = models.CharField(unique= True)
    subtitle = models.CharField()
    description = models.TextField()
    notes_types = models.TextField(choices = NOTES_TYPES)
    notes_desc = models.TextField()
    file = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnail/')
    instructor = models.ForeignKey(Tutor, on_delete=models.CASCADE,related_name="tutor" )
    course_overview = models.TextField()
    key_learnings = models.TextField()
    
    

    
