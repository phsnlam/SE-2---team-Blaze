from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import login, logut

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form' : form })


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            #log user in
            user = form.get_user()

            return redirect('article:list')


    else:
        form = AuthenticationForm()
    return render(request,"accounts/login.html",{'form':form})


def logout_view(request):
    if request.method =='POST'
        logout(request)
        return redirect('')
