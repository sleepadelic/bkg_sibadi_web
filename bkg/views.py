from django.http import HttpResponse
from django.shortcuts import render
from bkg.models import Issue
# Create your views here.
def index(request):
    iss = Issue.objects.all()
    context = {'problems_count': 66, 'resolved_problems': 55, 'iss':iss}

    return render(request, 'index.html', context)


def send_issue(request):
    return HttpResponse("send_issue")
def issues_list(request):
    return HttpResponse("list_of_issues")
