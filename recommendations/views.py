# recommendations/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Mock job postings data
JOB_POSTINGS = [
    {
        "job_id": 1,
        "job_title": "Software Engineer",
        "company": "Tech Solutions Inc.",
        "required_skills": ["JavaScript", "React", "Node.js"],
        "location": "San Francisco",
        "job_type": "Full-Time",
        "experience_level": "Intermediate"
    },
    {
        "job_id": 2,
        "job_title": "Data Scientist",
        "company": "Data Analytics Corp.",
        "required_skills": ["Python", "Data Analysis", "Machine Learning"],
        "location": "Remote",
        "job_type": "Full-Time",
        "experience_level": "Intermediate"
    },
    # ... other job postings ...
]

class JobRecommendationView(APIView):
    def post(self, request):
        user_profile = request.data

        # Extract user preferences
        user_skills = user_profile.get("skills", [])
        desired_roles = user_profile.get("preferences", {}).get("desired_roles", [])
        desired_locations = user_profile.get("preferences", {}).get("locations", [])
        desired_job_type = user_profile.get("preferences", {}).get("job_type", "Full-Time")
        experience_level = user_profile.get("experience_level", "Intermediate")

        # Filter job postings based on user profile
        recommendations = [
            {
                "job_title": job["job_title"],
                "company": job["company"],
                "location": job["location"],
                "job_type": job["job_type"],
                "required_skills": job["required_skills"],
                "experience_level": job["experience_level"]
            }
            for job in JOB_POSTINGS
            if (job["job_title"] in desired_roles or user_skills) and \
               (job["location"] in desired_locations or job["location"] == "Remote") and \
               (job["job_type"] == desired_job_type) and \
               (job["experience_level"] == experience_level)
        ]

        return Response(recommendations, status=status.HTTP_200_OK)
