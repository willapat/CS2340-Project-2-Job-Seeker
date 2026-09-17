from django.http import HttpResponse


def index(request):
    return HttpResponse("Job Seeker app is running.")
