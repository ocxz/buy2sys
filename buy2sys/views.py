from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name = request.session.get('name')
    isLogin = request.session.get('name')
    context = {}
    if isLogin:
        context['name'] = name
        context['isLogin'] = True
    return render(request, 'index.html', context=context)

def ajax_test(request):
    user_name = request.POST.get("username")
    password = request.POST.get("password")
    print(user_name, password)
    print('执行了')
    return HttpResponse("OK")

def ajax_load(request):
    return render(request, 'ajax.html')