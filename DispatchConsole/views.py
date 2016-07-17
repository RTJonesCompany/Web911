from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
#this index loads a example template with snippets {ryan}
def index(request):
    return render(request,'main/example.html')
