from django.http import HttpResponse
from django.shortcuts import render
from jobs.models import Job

def index(request):
    return HttpResponse("Job Seeker app is running.")

def job_search(request):
    jobs = Job.objects.all()

    title = request.GET.get('title', '').strip()
    skills = request.GET.get('skills', '').strip()
    location = request.GET.get('location', '').strip()
    salary_min = request.GET.get('salary_min', '').strip()
    salary_max = request.GET.get('salary_max', '').strip()
    remote = request.GET.get('remote', '').strip()
    visa_sponsorship = request.GET.get('visa_sponsorship')

    if title:
        jobs = jobs.filter(title__icontains=title)

    if skills:
        for skill in [s.strip() for s in skills.split(',') if s.strip()]:
            jobs = jobs.filter(skills__icontains=skill)

    if location:
        jobs = jobs.filter(location__icontains=location)

    if salary_min.isdigit():
        jobs = jobs.filter(salary_min__gte=int(salary_min))

    if salary_max.isdigit():
        jobs = jobs.filter(salary_max__lte=int(salary_max))

    if remote == 'true':
        jobs = jobs.filter(remote=True)
    elif remote == 'false':
        jobs = jobs.filter(remote=False)

    if visa_sponsorship == 'on':
        jobs = jobs.filter(visa_sponsorship=True)

    return render(request, 'job_seeker/job_search.html', {
        'jobs': jobs,
        'filters': request.GET,
        'remote_selected': remote == 'true',
        'onsite_selected': remote == 'false',
        'visa_checked': visa_sponsorship == 'on',
    })
