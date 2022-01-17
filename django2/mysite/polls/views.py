from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Theme, Question
from django.http import Http404


def index(request):
    latest_theme_list = Theme.objects.order_by('id')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_theme_list': latest_theme_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, theme_id):
    question_list = Question.objects.order_by('theme_id')[:5]
    context = {
        'question_list': question_list,
    }
    return render(request, 'polls/detail.html', context)