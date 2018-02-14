from django.shortcuts import render
from first_web_app.forms import UserForm, UserProfileInfoForm
# Create your views here.
def index(request):
    return render(request,'first_web_app/index.html')
