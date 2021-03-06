from django.shortcuts import render, redirect, Http404, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import infoForm
from . models import MyUser
from django.contrib.auth.models import User

def signup_view(request):
    request.session['user_id'] = None
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            user = User.objects.get(username = username)
            request.session['user_id'] = user.id
            return redirect('accounts:userInfo')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form' : form })


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            #log user in
            user = form.get_user()
            login(request,user)
            request.session['user_id'] = user.id
            try:
                my_user = user.myuser
            except:
                return redirect("accounts:userInfo")
            return redirect('../../rolechoice')
    else:
        form = AuthenticationForm()
    return render(request,"accounts/login.html",{'form':form})

def logout_view(request):
    logout(request)
    request.session['user_id'] = None
    return redirect("Home:Home")

def forgot_view(request):
    return render(request,"accounts/forgot.html")

def get_user_info(request):
    try:
        user_id = request.session['user_id']
        if user_id is not None:
            form = infoForm(request.POST)
            if form.is_valid():
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                email = form.cleaned_data['email']
                if user_id is not None:
                    user = User.objects.get(id = user_id)
                    request.session['user_id'] = None
                    my_user = MyUser(email = email, last_name = last_name, first_name = first_name, user = user)
                    my_user.save()
                else:
                    raise Http404
                return redirect('Home:Home')
            return render(request, 'accounts/get_info.html', {'form' : form})
        else:
            return Http404
    except:
        return redirect("Home:Home")
