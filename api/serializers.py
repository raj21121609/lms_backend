from rest_framework import serializers
from .models import Tutor
from .models import Courses

class Tutor_profile_serializers(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ['first_name','last_name','headline','tutor_description','language','image_label','profile_pic','areas_of_experience','professional_experience','website','x','linkdin','youtube','facebook'] 
        
class Courses_serializers(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['price','title','about_course','course_description','certification','instructor',
                  'thumbnail','language']