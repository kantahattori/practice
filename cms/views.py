from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'cms/top.html')
    # return HttpResponse('10キロ痩せます...')
def list(request, id=None):
    if id:
        print(id)
    else:
        id = ''
    dict = {'id': id}
    return render(request, 'cms/list.html', dict)
