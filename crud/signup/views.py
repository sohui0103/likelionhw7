from django.shortcuts import render, redirect, get_object_or_404
from .models import Signup
from django.utils import timezone

# Create your views here.
def home(request):
    blogs = Signup.objects.all()
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, id):
    blog = get_object_or_404(Signup, pk=id)
    return render(request, 'detail.html', {'blog':blog})

def new(request):
    return render(request, 'new.html')

def create(request):
    new_blog = Signup()
    new_blog.name = request.POST['name']
    new_blog.age= request.POST['age']
    new_blog.email= request.POST['email']
    new_blog.pub_date = timezone.now()
    new_blog.introduce = request.POST['introduce']
    new_blog.save()
    return redirect('detail', new_blog.id)

def edit(request, id):
    edit_blog = Signup.objects.get(pk=id)
    return render(request, 'edit.html', {'blog':edit_blog})

def update(request, id):
    update_blog = Signup.objects.get(pk=id)
    update_blog.name = request.POST['name']
    update_blog.age = request.POST['age']
    update_blog.email = request.POST['email']
    update_blog.pub_date = timezone.now()
    update_blog.introduce = request.POST['introduce']
    update_blog.save()
    return redirect('detail', str(update_blog.id))

def delete(request, id):
    delete_blog = Signup.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')