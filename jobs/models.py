from django.db import models
from django.contrib.auth.models import User
#from accounts.models import Skill

# Create your models here.
class Job(models.Model):
    id = models.AutoField(primary_key=True)
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    company = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    remote = models.BooleanField(default=False)
    location = models.CharField(max_length=255) #may need to make this work with google maps later
    skills = models.TextField(blank=True, default='')
    visa_sponsorship = models.BooleanField(default=False)
    #removed = models.BooleanField(default=False)
    def __str__(self):
        return str(self.id) + ' - ' + self.company + ' - ' + self.title