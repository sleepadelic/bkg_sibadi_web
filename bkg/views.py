from django.http import HttpResponse
from django.shortcuts import render
from bkg.models import Issue


# Create your views here.
def index(request):
    published_issues = Issue.objects.all().filter(is_published=True)
    last_resolved_issues = Issue.objects.all().filter(is_published=True).filter(status__name='Решено')[:10]
    context = {'problems_count': 66, 'resolved_problems': 55, 'iss': published_issues,
               'last_resolved_issues': last_resolved_issues}
    return render(request, 'index.html', context)


def send_issue(request):
    return HttpResponse("send_issue")


def issues_list(request):
    published_issues = Issue.objects.all().filter(is_published=True).exclude(status__name='Решено')[0:30]
    resolved_issues = Issue.objects.all().filter(is_published=True).filter(status__name='Решено')[0:20]
    context = {'iss': published_issues,
               'resolved_issues': resolved_issues, 'next_page_num': 1}
    return render(request, 'citizensAppeals.html', context)


def issues_list_page(request, page_num):
    published_issues = Issue.objects.all().filter(is_published=True).exclude(status__name='Решено')[
                       31 + 30 * page_num:31 + 30 * page_num * 10 + 30]
    resolved_issues = Issue.objects.all().filter(is_published=True).filter(status__name='Решено')[
                      20 + 20 * page_num:31 + 30 * page_num + 20]
    context = {'iss': published_issues,
               'resolved_issues': resolved_issues, 'page_num': page_num, 'next_page_num': page_num + 1,
               'prev_page_num': page_num - 1, }

    return render(request, 'citizensAppeals.html', context)
