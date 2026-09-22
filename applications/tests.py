from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.urls import reverse

from jobs.models import Job
from .models import Application


class ApplicationTests(TestCase):

    def setUp(self):
        self.recruiter = User.objects.create_user(
            username='recruiter',
            password='testpass123'
        )

        self.applicant = User.objects.create_user(
            username='applicant',
            password='testpass123'
        )

        self.job = Job.objects.create(
            recruiter=self.recruiter,
            company='Test Company',
            title='Software Engineer',
            description='Test job description',
            salary_min=50000,
            salary_max=70000,
            remote=True,
            location='Atlanta',
            visa_sponsorship=False
        )

    def test_user_can_apply_with_note(self):
        self.client.login(
            username='applicant',
            password='testpass123'
        )

        response = self.client.post(
            reverse('applications.apply', args=[self.job.id]),
            {'note': 'I am a great fit for this position.'}
        )

        self.assertEqual(Application.objects.count(), 1)

        application = Application.objects.first()

        self.assertEqual(application.applicant, self.applicant)
        self.assertEqual(application.job, self.job)
        self.assertEqual(
            application.note,
            'I am a great fit for this position.'
        )

    def test_user_cannot_apply_twice(self):
        self.client.login(
            username='applicant',
            password='testpass123'
        )

        url = reverse('applications.apply', args=[self.job.id])

        self.client.post(url, {'note': 'First application'})
        self.client.post(url, {'note': 'Second application'})

        self.assertEqual(Application.objects.count(), 1)