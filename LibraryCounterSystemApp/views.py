from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import User
from django.contrib.auth import authenticate, logout, login as auth_login


# Create your views here.
def login_page(request):
    return render(request, 'login.html')


def user_page(request):
    return render(request, 'add-user.html')


def addUser(request):
    pic = request.POST.get('pic')
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    if request.method == 'POST':
        user = User.objects.create(firstname=firstname, lastname=lastname, email=email, password=password)
        user.save()
        messages.success(request, 'Successfully Registered')
        return redirect('user')


def delete_data(request, id):
    try:
        pi = User.objects.get(pk=id)
        if pi.isActive is True:
            pi.isActive=False
            pi.save()
            messages.success(request, 'User delete successfully!')
            return redirect('user')
    except:
        messages.error(request, 'Failed to delete user')
        return redirect('user')


def update_data(request, user_id):
    context = {
        'userinfo': User.objects.get(id=user_id),
        'user_id': user_id
    }
    return render(request, 'edit_assistant.html', context)


def save_edit_user(request):
    user_id = request.POST.get('user_id')
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    # email = request.POST.get('email')
    password = request.POST.get('password')
    # try:
    #     user = User.objects.get(user_id)
    #     print(user.id)
    #     user.firstname = firstname
    #     user.lastname = lastname
    #     user.email = email
    #     user.password = password
    #     user.save()
    #     messages.success(request, 'Successfully updated')
    #     return redirect('user')
    # except:
    #     messages.error(request, 'Failed to save edit information')
    #     return redirect('user')
    user = User.objects.get(id=user_id)
    user.firstname = firstname
    user.lastname = lastname
    user.password = password
    user.save()
    messages.success(request, 'Successfully updated')
    return redirect('user')


# Create your views here.
def sign_page(request):
    return render(request, 'user')


# Create your views here.
def register(request):
    domain = ['gift.edu.pk']
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exist!")
            return redirect('signup')
        elif email not in domain:
            messages.error(request, 'Please fill with correct domain')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exist!")
            return redirect('signup')
        elif User.objects.filter(password=password).exists():
            messages.error(request, "Password already exist!")
            return redirect('signup')
        elif password != confirmpassword:
            messages.error(request, "Mismatch password")
            return redirect('signup')
    try:
        user = User.objects.create(username=username, password=password, email=email)
        user.save()
        messages.success(request, 'Successfully Registered')
        return redirect('signup')
    except:
        messages.error(request, 'Sign Up Failed')
        return redirect('signup')


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')


def profile(request):
    return render(request, 'profile.html')


def reports(request):
    return render(request, 'reports.html')


def setting(request):
    return render(request, 'setting.html')


def assistant(request):
    userlist = User.objects.all()
    context = {
        'userlist': userlist
    }
    return render(request, 'user.html', context)


def visitors(request):
    return render(request, 'visitors.html')
