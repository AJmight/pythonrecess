from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
def home(request):
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")

class login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        # Handle login logic here
        return HttpResponse("Login successful")  # Placeholder response