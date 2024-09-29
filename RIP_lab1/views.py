from django.shortcuts import render
def MainPage_Render(request):
    return render(request, 'index.html')