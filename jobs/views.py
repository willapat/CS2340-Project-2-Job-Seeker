from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from django.contrib.auth.decorators import login_required
from .forms import JobForm
from applications.models import Application

# Create your views here.
def index(request):
# def index(request):
    #job list and search (US2) are merged here
    #filters come from the search form that was moved to job_list.html
    #moved here from the job_search() method in job_seeker/views.py
    jobs = Job.objects.all()

    #Zane's search code (US2)
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

    template_data = {}
    template_data['jobs'] = jobs
    template_data['filters'] = request.GET
    template_data['remote_selected'] = remote == 'true'
    template_data['onsite_selected'] = remote == 'false'
    template_data['visa_checked'] = visa_sponsorship == 'on'
    return render(request, 'jobs/job_list.html', {'template_data': template_data})

    # template_data = {}
    # #template_data['title'] = 'Jobs'
    # template_data['jobs'] = Job.objects.all()
    # return render(request, 'jobs/job_list.html', {'template_data': template_data})

def show(request, id):
    job = get_object_or_404(Job, id=id)
    template_data = {}
    #template_data['title'] = job.title
    template_data['job'] = job
    if request.user.is_authenticated:
        applications = Application.objects.filter(applicant=request.user,job=job)
        if applications:
            template_data['has_applied'] = True
        else:
            template_data['has_applied'] = False
    else:
        template_data['has_applied'] = False
    return render(request,'jobs/job_detail.html',{'template_data':template_data})
    

@login_required
def create(request):
    template_data = {}
    template_data['title'] = 'Post a Job'
    if request.method == 'GET':
        template_data['form'] = JobForm() #get a blank form for a get request
        return render(request, 'jobs/job_form.html', {'template_data': template_data})
    elif request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit = False)
            job.recruiter = request.user
            job.save()
            return redirect('jobs.index')
        else:
            template_data['form'] = form
            return render(request, 'jobs/job_form.html', {'template_data': template_data})

@login_required
def edit(request, id):
    job = get_object_or_404(Job, id=id)
    if request.user != job.recruiter:
        return redirect('jobs.show', id=id)
    template_data = {}
    #template_data['title'] = 'Edit Job'
    if request.method == 'GET':
        template_data['form'] = JobForm(instance=job)
        return render(request, 'jobs/job_form.html', {'template_data': template_data})
    elif request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('jobs.show', id=id)
        else:
            template_data['form'] = form
            return render(request, 'jobs/job_form.html', {'template_data': template_data})

# def apply(request): 
#     return
#apply is in view