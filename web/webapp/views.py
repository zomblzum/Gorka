from django.shortcuts import render

def index(request):
    return render(request, 'webapp/index.html')

def test(request):
    return render(request, 'webapp/test.html', {'data':[1,2]})