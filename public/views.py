from django.shortcuts import render

def index(request):
    context = {
        'title' : "Homepage",
        'desc' : 'Welcome to Homepage'
    }
    return render(request, 'public/index.html', context)
