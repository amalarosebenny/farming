from django.http import HttpResponse
from django.shortcuts import render, redirect
from  .models import movie
from .forms import movieforms
# Create your views here.
def index(request):
    movie_1=movie.objects.all()
    context={
        'movie_list':movie_1
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    movie_2=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':movie_2})
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        year=request.POST.get('year')
        img=request.FILES['img']
        movie_1=movie(name=name,desc=desc,year=year,img=img)
        movie_1.save()
    return render(request,'add.html')
def update(request,id):
    movie_1=movie.objects.get(id=id)
    form=movieforms(request.POST or None,request.FILES,instance=movie_1)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie_1':movie_1})
def delete(request,id):
    if request.method=='POST':
        movie_1=movie.objects.get(id=id)
        movie_1.delete()
        return redirect('/')
    return render(request,'delete.html')