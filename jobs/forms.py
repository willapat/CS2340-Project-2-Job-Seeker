from django import forms
from accounts.forms import BootstrapMixin
from .models import Job

class JobForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'remote', 'salary_min', 'salary_max', 'visa_sponsorship', 'description']
        labels = {
            'remote': 'Remote',
            'salary_min': 'Minimum salary: $',
            'salary_max': 'Maximum salary: $',
            'visa_sponsorship': 'Available',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows':6}),
        }