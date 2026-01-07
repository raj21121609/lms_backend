from rest_framework import serializers
from .models import Tutor

class Tutor_profile_serializers(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ['first_name','last_name','headline','tutor_description','image_label','profile_pic','areas_of_experience','professional_experience','website','x','linkdin','youtube','facebook'] 