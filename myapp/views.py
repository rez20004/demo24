from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.
from . forms import RegistrationForm


def index(request):

    form = RegistrationForm()
    context = {
         "myregistrationform": form
    }
    return render(request, 'myapp/index.html', context)


def protected_view(request):
    return render(request, 'myapp/index.html', {'current.user': request.user})