from django.shortcuts import render,redirect
from django.contrib.auth import authenticate



# Create your views here.

def index(request):
    if request.method == "POST":
        password = request.POST.get('password')
        college_id = request.POST.get('collegeId')
        fin_year = request.POST.get('finincialyear')
        
        user = authenticate(college_id=college_id,password=password)
        if user:
            return redirect("/home")
        else:
            error_message = "Authentication failed. Please check your credentials."
            return render(request, 'index.html', {'error_message': error_message})
   
    return render(request,'index.html')


def home(request):
    return render(request,'home.html')



def createUser(request):
    pass

