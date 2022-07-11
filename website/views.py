from django.shortcuts import render, redirect, reverse
from django.contrib.auth import logout
from multiprocessing import context
from django.contrib import messages
from django.views import generic
from .models import *
from .form import *

def home(request):
    return render(request, 'home.html')

def premium(request):
    fun = Pro.objects.all()
    context = {
        "base":fun
    }
    return render(request, "pro/premium.html", context)

def team(request):
    fun = Team.objects.all()
    context = {
        "base":fun
    }
    return render(request, "team/team.html", context)

def chart(request):
    fun = Chart.objects.all()
    context = {
        "base": fun
    }
    return render(request, 'charts/chart.html', context)



def contact(request):
    if request.method == "POST":
        form = ContactUs(request.POST)
        if form.is_valid():
            form.save()
            return redirect("app:succses")
    else:
        form = ContactUs()
    return render(request, "contactus/contact.html", {'form': form})

def Subscibe(request):
    fun = Pro.objects.all()
    context = {
        "base": fun
    }
    return render(request, "pro/subscribe.html", context)

class Succses(generic.TemplateView):
    template_name = 'succses.html'



class Unfortunate(generic.TemplateView):
    template_name = 'unfortunate.html'

class Notifactions(generic.TemplateView):
    template_name = 'notifaction.html'

class Sign(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = SignUp
    def get_success_url(self):
        return reverse("login")
    
def addChart(request):
    if request.method == "POST":
        form = AddChart(request.POST)
        if form.is_valid():
            form.save()
            return redirect("app:chart")
    else:
        form = AddChart()
    return render(request, 'charts/addchart.html', {"form": form})


def logout_user(request):
    logout(request)
    messages.success(request, "Your was logout")
    return redirect('/')