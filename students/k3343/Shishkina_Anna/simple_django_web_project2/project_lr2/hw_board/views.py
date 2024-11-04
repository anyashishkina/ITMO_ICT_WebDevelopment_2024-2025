from django.shortcuts import render, redirect
from .forms import RegistrationForm, HwSubmissionForm
from .models import Hw
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

def home_view(request):
    return render(request, 'home.html')  # Создайте home.html для отображения главной страницы


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})




def hw_list(request):
    hws = Hw.objects.all()
    return render(request, 'hw_list.html', {'hws': hws})


def submit_hw(request):
    if request.method == 'POST':
        form = HwSubmissionForm(request.POST)
        if form.is_valid():
            hw_submission = form.save(commit=False)
            hw_submission.user = request.user
            hw_submission.save()
            return redirect('hw_list')
    else:
        form = HwSubmissionForm()
    return render(request, 'submit.html', {'form': form})

