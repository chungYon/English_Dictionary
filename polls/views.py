from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Word


def index(request):
    # latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html')


# def index(request):
#     latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {'latest_question_list': latest_question_list}
#     return HttpResponse(template.render(context, request))


# def index(request):
#     latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in latest_question_list])
#     return HttpResponse(output)


# def index(request):
#     return HttpResponse("Hello world! You're at the polls index.")


def detail(request, word_id):
    word = get_object_or_404(Word, pk=word_id )
    meanings = word.meaning_text.split(',')
    cnt = 0
    for meaning in meanings:
        meanings[cnt] = meaning.replace(';', ', ')
        cnt += 1
    synonyms = word.synonym_text.split(',')
    return render(request, 'polls/detail.html', {'word': word, 'meanings': meanings, 'synonyms': synonyms})


def detail_str(request, word_text):
    word = get_object_or_404(Word, word_text=word_text)
    meanings = word.meaning_text.split(',')
    cnt = 0
    for meaning in meanings:
        meanings[cnt] = meaning.replace(';', ', ')
        cnt += 1
    synonyms = word.synonym_text.split(',')
    return render(request, 'polls/detail.html', {'word': word, 'meanings': meanings, 'synonyms': synonyms})

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist.")
#     return render(request, 'polls/detail.html', {'question': question})

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)


def results(request):

    if 'q' in request.POST:
        query = request.POST.get('q', False)
        words = Word.objects.all().filter(word_text__contains=query)
    return render(request, 'polls/results.html', {'words': words, 'query': query})


# def results(request, question_id):
#     return HttpResponse("You're looking at results of question %s." % question_id)


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice."
#         })
#     selected_choice.votes += 1
#     selected_choice.save()
#     return HttpResponseRedirect(reverse('polls:results', args=(question.id, )))

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)






