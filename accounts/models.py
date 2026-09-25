from django.db import models

# Create your models here.
from django.conf import settings


class SkillChoice(models.TextChoices):
    PROGRAMMING = "programming", "Programming"
    DESIGN = "design", "Design"
    MARKETING = "marketing", "Marketing"
    FRONTEND = "frontend", "Frontend"
    BACKEND = "backend", "Backend"
    FULLSTACK = "fullstack", "Fullstack"
    MOBILE_DEVELOPMENT = "mobile_development", "Mobile Development"
    WEB_DEVELOPMENT = "web_development", "Web Development"
    COMMUNICATION = "communication", "Communication"
    TEAMWORK = "teamwork", "Teamwork"
    ORGANIZATION = "organization", "Organization"
    DATABASE_DESIGN = "database_design", "Database Design"
    SALES = "sales", "Sales"
    LEADERSHIP = "leadership", "Leadership"


class Profile(models.Model):
    class roles(models.TextChoices):
        RECRUITER = "recruiter", "Recruiter"
        CANDIDATE = "candidate", "Candidate"

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=roles.choices, default=roles.CANDIDATE)
    headline = models.CharField(max_length=200, blank=True)
    skills = models.JSONField(default=list, blank=True)
    role = models.CharField(max_length=20, choices=roles.choices, default=roles.CANDIDATE)

    def __str__(self):
        return f"{self.user}'s profile"
    
    @property
    def is_recruiter(self):
        return self.role == self.roles.RECRUITER
    
    @property
    def is_candidate(self):
        return self.role == self.roles.CANDIDATE


class Education(models.Model):
    profile = models.ForeignKey(Profile, related_name="education", on_delete=models.CASCADE)
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=200, blank=True)
    start_year = models.PositiveIntegerField(null=True, blank=True)
    end_year = models.PositiveIntegerField(null=True, blank=True)


class WorkExperience(models.Model):
    profile = models.ForeignKey(Profile, related_name="experience", on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # null = current job
    description = models.TextField(blank=True)


class Link(models.Model):
    profile = models.ForeignKey(Profile, related_name="links", on_delete=models.CASCADE)
    label = models.CharField(max_length=50)
    url = models.URLField()