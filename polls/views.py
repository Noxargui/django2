# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import get_object_or_404, render
from .models import Theme, Question, Choice
from django.http import Http404


def index(request):
    latest_theme_list = Theme.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    context = {
        'latest_theme_list': latest_theme_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context)

def detail(request, theme_id):
    latest_question_list = Question.objects.filter(theme=theme_id)
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/detail.html', context)
    # question = get_object_or_404(Theme, pk=question_id)
    # return render(request, 'polls/detail.html', {'question': question})
    
def response(request, question_id):
    latest_choice_list = Choice.objects.filter(question=question_id)
    context = {
        'latest_choice_list': latest_choice_list,
    }
    return render(request, 'polls/response.html', context)