from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User,auth
from .forms import PersonCreationForm
from .models import Person, Course
# Create your views here.

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('accounts:page1')
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:
        return render(request,'login.html')


def register(request):
    if request.method=='POST':
        first_name=request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                messages.info(request,'User created')
        else:
            messages.info(request,'password not matched')
            return redirect('accounts:register')
        return redirect('accounts:login')
    else:
        return render(request,'registration.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
def page1(request):
    return render(request,'page1.html')
def create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:msg')
    return render(request,'page2.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request,'page2.html', {'form': form})
def load_cities(request):
    department_id = request.GET.get('department')
    courses = Course.objects.filter(department_id=department_id).all()
    return render(request,'page3.html', {'courses': courses})
    # print(list(courses.values('id', 'name')))
    # return JsonResponse(list(courses.values('id', 'name')), safe=False)
def msg(request):
    return render(request,'msg.html')