from django.db import models

# Create your models here.
from django.conf import settings


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=200, blank=True)
    skills = models.ManyToManyField(Skill, blank=True, related_name="profiles")

    def __str__(self):
        return f"{self.user}'s profile"


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