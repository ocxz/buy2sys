from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse
from . import models

# Create your views here.

def login(request):
    name = request.session.get('name')
    context = {}
    if name:
        context['name'] = name
    return render(request, 'login.html', context=context)

def logout(request):
    request.session['name']=''
    request.session['isLogin'] = ''
    return redirect(reverse('index'))

def dologin(request):
    name = request.POST.get('username')
    request.session['name'] = name
    password = request.POST.get('password')
    users = models.User.objects.filter(name=name)
    if users and users[0].password == password:
        request.session['isLogin'] = True
    else:
        request.session['isLogin'] = True
    return redirect(reverse('index'))
def register(request):
    return render(request, 'zhuce.html')

def doregister(request):
    name = request.POST.get('name')
    password = request.POST.get('pw')
    request.session['name'] = name
    user = models.User(name=name, password=password)
    user.save()
    # request.session['name'] = name
    return redirect(reverse('user:login'))

def isRegistered(request):
    username = request.POST.get('username')
    users = models.User.objects.filter(name=username)
    print("执行了")
    if users:
        print('Registered is true')
        return HttpResponse("Yes")
    else:
        print('Registered is false')
        return HttpResponse("No")