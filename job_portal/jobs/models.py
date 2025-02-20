# jobs/models.py
from django.db import models

# User Model (can use Django's User model or extend it)
class User(models.Model):
    ROLE_CHOICES = [
        ('job_seeker', 'Job Seeker'),
        ('employer', 'Employer'),
    ]
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    role = models.CharField(choices=ROLE_CHOICES, max_length=20)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.username


# Job Model
class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    required_skills = models.TextField()
    salary_range = models.CharField(max_length=255)
    experience_required = models.CharField(max_length=255)
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')

    def __str__(self):
        return self.title


# Resume Model
class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resumes')
    resume_file = models.FileField(upload_to='resumes/')
    skills = models.TextField()  # Extracted skills
    experience = models.TextField()  # Extracted experience
    education = models.TextField()  # Extracted education

    def __str__(self):
        return f'{self.user.username} Resume'
