"""
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
            try:
                user = form.save()
                print(user)
                if user is not None:
                    return redirect('login')
            except:
                return render(request , 'signup.html' , context=context)
        else:
            return render(request , 'signup.html' , context=context)
"""


"""def signup(request):
    try:
        print(request.POST)
        form = UserCreationForm(request.POST)  
        context = {
            "form" : form
        }
        if form.is_valid():
            try:
                user = form.save()
                #print(user)
                if user is not None:
                    return redirect('login')
            except:
                return render(request , 'signup.html' , context=context)
        else:
            return render(request , 'signup.html' , context=context)
    except:
        if request.method == 'GET':
            form = UserCreationForm()
            context = {
                "form" : form
            }
            return render(request , 'signup.html' , context=context)"""


"""def login(request):
    try:
        form = AuthenticationForm(data=request.POST)
        #print(form.is_valid())
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
    except:
        if request.method == 'GET':
            form = AuthenticationForm()
            context = {
                "form" : form
            }
            return render(request , 'login.html' , context=context )
            """

"""
def change_todo(request , id  , status):
    todo = TODO.objects.get(pk = id)
    todo.status = status
    todo.save()
    return redirect('home')
"""