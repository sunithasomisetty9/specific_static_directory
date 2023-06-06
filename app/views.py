from django.shortcuts import render

# Create your views here.

def specific_static_directory(request):
    return render(request, 'specific_static_directory.html')