from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.


from jobs.models import Job
from .models import Application


@login_required

def apply(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if Application.objects.filter(
        applicant=request.user,
        job=job
    ).exists():
        return redirect('jobs.show', id=job.id)
    if request.method == 'GET':
        template_data = {}
        template_data['job'] = job

        return render(
            request,
            'applications/apply.html',
            {'template_data': template_data}
        )

    elif request.method == 'POST':
        note = request.POST.get('note', '')

        Application.objects.create(
            applicant=request.user,
            job=job,
            note=note
        )

        return redirect('jobs.show', id=job.id)