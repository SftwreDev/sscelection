from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Question, Choice

class BaseView(generic.ListView):
	model = Question
	template_name = "polls/vote.html"
	context_object_name = 'latest_question_list'

	

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/result.html'


def vote (request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/vote.html', {'error_message' : "You didn't select your vote", })
	else:
		selected_choice.votes +=1
		selected_choice.save()
		return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))