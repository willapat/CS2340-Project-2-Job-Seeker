from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from django.contrib.auth.decorators import login_required
from .forms import JobForm

# Create your views here.
def index(request):
    template_data = {}
    #template_data['title'] = 'Jobs'
    template_data['jobs'] = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'template_data': template_data})

def show(request, id):
    job = Job.objects.get(id=id)
    template_data = {}
    #template_data['title'] = job.title
    template_data['job'] = job
    return render(request, 'jobs/job_detail.html', {'template_data': template_data})

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