from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.template import loader
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'question': question,
            'error_message': 'You did not select a choice.',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls_name:results', args=(question.id,)))


def add_new_choice(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        candidate = request.POST.get('new_name')
        if not candidate:
            raise KeyError
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {'question': question,
                                               'error_message': 'You did not make new choice'})
    else:
        choices = question.choice_set.create(choice_text=candidate, votes=0)
        return HttpResponseRedirect(reverse('polls_name:detail', args=(question.id,)))


