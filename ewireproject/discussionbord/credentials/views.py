from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['name']
        email = request.POST['email']
        #mobile = request.POST['mobile']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if not first_name or not email  or not username or not password:
            #messages.error(request, "Please fill in all the fields.")
            return redirect('credentials:register')
        if len(password) < 8:
            messages.info(request, "Password must be at least 8 characters long")

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "User Taken")
                return redirect('credentials:register')
            else:
                user = User.objects.create_user(first_name=first_name,email=email,username=username, password=password)
                user.save()
                messages.success(request, "Registration successful. Please log in.")
                return redirect('credentials:login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('credentials:register')

    return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('post:postlogin')
        else:
            messages.info(request, "invalid Credentials")
            return redirect('login')

    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('credentials:register')