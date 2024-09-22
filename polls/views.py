from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

added_polls = []

def index(request):
    return render(request, "polls/index.html", {
        "added_polls": added_polls
    })

def addpoll(request):
    content = request.POST.get('form_content')
    added_polls.append(content)
    return render(request, "polls/addpoll.html", {
        "content": content,
        "added_polls": added_polls
    })
