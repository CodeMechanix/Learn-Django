from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

            

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
