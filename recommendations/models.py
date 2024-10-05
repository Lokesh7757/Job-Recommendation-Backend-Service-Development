from django.db import models

class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    skills = models.JSONField()  # Store skills as a list
    experience_level = models.CharField(max_length=50)
    preferences = models.JSONField()  # Store preferences as a dict

class JobPosting(models.Model):
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    required_skills = models.JSONField()  # Store skills as a list
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50)
    experience_level = models.CharField(max_length=50)
