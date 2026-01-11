from django.db import models
from django.contrib.auth.models import User

class Tutor(models.Model):
    LANGUAGES = [
        ('English','English'),
        ('Spanish','Spanish'),
        ('Italian','Italian'),
        ('German','German'),
        ('French','French')
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    headline = models.CharField(max_length=30,blank=True)
    tutor_description = models.CharField(default="")
    language = models.CharField( choices=LANGUAGES, default='EN')
    image_label = models.CharField( max_length=20,default="profile")
    profile_pic = models.ImageField(upload_to='pics/')
    
    #extra's    
    areas_of_experience = models.TextField(default="")
    professional_experience = models.TextField(default="")
    
    #links 
    website = models.URLField(null=True,blank=True)
    x = models.URLField(null=True,blank=True)
    linkdin = models.URLField(null=True,blank=True)
    youtube = models.URLField(null=True,blank=True)
    facebook = models.URLField(null=True,blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True,null=True,
        blank=True)

    def __str__(self):
        return self.first_name

class Courses(models.Model):
    NOTES_TYPES = [
        ('PD','PDF'),
        ('PT','PPT')
    ]
    price = models.IntegerField(default=0)
    title = models.CharField(unique= True)
    subtitle = models.CharField()
    description = models.TextField()
    notes_types = models.CharField(choices = NOTES_TYPES)
    notes_desc = models.TextField()
    file = models.FileField(upload_to='course_files/')
    thumbnail = models.ImageField(upload_to='thumbnail/',null=True,blank=True)
    instructor = models.ForeignKey(Tutor, on_delete=models.CASCADE,related_name="tutor" )
    course_overview = models.TextField(default="")
    key_learnings = models.TextField(default="")
    
    created_at = models.DateTimeField(auto_now_add=True,null=True,
        blank=True)
    
    def __str__(self):
        return self.title
    
class Chapters(models.Model):
    title = models.TextField(default="")
    subtitle = models.TextField(default="")
    desciption = models.TextField(default="")
    notes_content_type = models.CharField()
    notes_type = models.TextField()
    notes_description = models.TextField()
    file = models.FileField()
    thumbnail = models.ImageField()
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
    course = models.ForeignKey(Courses,on_delete=models.CASCADE,related_name='course_table',default="")
    
    created_at = models.DateTimeField(auto_now_add=True,null=True,
        blank=True)
    
    def __str__(self):
        return self.student_user