from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.utils import timezone
from travello.models import Roleurl
from django.contrib import messages
from django.http import HttpResponse
from django.core import serializers


from django.contrib.auth.decorators import login_required


def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']

        user = auth.authenticate(username=username, password=password)
        request.session['SessionName'] = user.is_staff

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def book(request):
    if(request.session['SessionName']):
        return render(request, 'booklist.html')
        # 
        # b = Roleurl.objects.filter(user_type="admin").values('valid_url')
        # return HttpResponse(b)
    else:
        return render(request,"error.html")
            
def home(request):
    # return HttpResponse(request.session['SessionName'])
    return render(request,"index.html")

def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['uname']
        email = request.POST['email']
        password = request.POST['psw']
        conf_password = request.POST['psw-repeat']
        if password == conf_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
                # print("Username Taken")
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
                # print("Email Taken")
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'User Created')
                return redirect('login')
                # print("User Created")
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('register')
            # print("Password Not Matching")
        return redirect('/')
    else:
        return render(request, 'register.html')
