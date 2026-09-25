from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
from accounts.decorators import job_seeker_required
from jobs.models import Job

@login_required
@job_seeker_required
def index(request):
    cart = request.session.get('cart', [])
    template_data = {}
    template_data['jobs'] = Job.objects.filter(id__in=cart)
    return render(request, 'cart/index.html', {'template_data': template_data})

@login_required
@job_seeker_required
def add(request, id):
    job = get_object_or_404(Job, id=id)
    if request.method == 'POST':
        cart = request.session.get('cart', [])
        if job.id not in cart:
            cart.append(job.id)
            request.session['cart'] = cart
        messages.success(request, 'Job added to your cart.')
    return redirect('jobs.show', id=job.id)

@login_required
@job_seeker_required
def remove(request, id):
    if request.method == 'POST':
        cart = request.session.get('cart', [])
        if id in cart:
            cart.remove(id)
            request.session['cart'] = cart
    return redirect('cart.index')