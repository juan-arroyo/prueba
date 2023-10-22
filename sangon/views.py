from django.shortcuts import render

# Create your views here.
def sangon(request):
    return render(request, 'sangon/index.html')