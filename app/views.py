
from xmlrpc.client import ResponseError
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login as loginUser , logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from app.forms import TODOForm
from app.models import TODO
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
#from django.contrib import messages


# Create your views here.
@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = TODOForm()
        todos = TODO.objects.filter(user = user).order_by('date_from')
        return render(request , 'index.html' , context={'form' : form , 'todos' : todos})


#user login
def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            "form" : form
        }
        return render(request , 'login.html' , context=context )
    else:
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            if user is not None:
                loginUser(request , user)
                return redirect('home')
        else:
            context = {
                "form" : form
            }
            return render(request , 'login.html' , context=context )



# View for user signup
def signup(request):

    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form" : form
        }
        return render(request , 'signup.html' , context=context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)  
        context = {
            "form" : form
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request , 'signup.html' , context=context)



# add task
@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo)
            return redirect("home")
        else: 
            return render(request , 'index.html' , context={'form' : form})


# delete the task
def delete_todo(request , id ):
    print(id)
    TODO.objects.get(pk = id).delete()
    return redirect('home')

# Update and Edit function
def update_data(request, id):
    if request.method == 'POST':
        pi = TODO.objects.get(pk = id)
        #form = UserCreationForm(request.POST, instance = pi)
        form = TODOForm(request.POST, instance = pi)
        if form.is_valid():
            form.save()
    else:
        pi = TODO.objects.get(pk = id)
        form = TODOForm(instance = pi)
    return render(request, 'updatedata.html', {'form':form})

#Signout
def signout(request):
    logout(request)
    return redirect('login')


def pending(request):
    
    
    return render(request, 'pending.html')


def completed(request):
    
    
    return render(request, 'completedtask.html')
