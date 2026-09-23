from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from jobs.models import Job

class Application(models.Model):
    
    applicant = models.ForeignKey(User,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    note = models.TextField(blank =True)
    
    date_applied = models.DateTimeField(auto_now_add= True)

    
    def _str_(self):
        return f"{self.applicant.username} -{self.job.title}"