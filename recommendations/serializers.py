from rest_framework import serializers
from .models import UserProfile, JobPosting  # Adjust as needed

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'  # or specify the fields you want to include

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields = '__all__'  # or specify the fields you want to include
