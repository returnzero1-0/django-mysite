from django.shortcuts import render
from django.http import HttpResponse    #if you use alternate way then you need to import this line
from .models import Question


def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    #output=', '.join([q.question_text for q in latest_question_list])

   # template=loader.get_template('polls/index.html') #alternate way
    context={
        'latest_question_list':latest_question_list,
    }

    #return HttpResponse(template.render(context,request)) #alternate way
    return render(request,'polls/index.html',context)

def detail(request,question_id):

#A shortcut: get_object_or_404()

    question=get_object_or_404(Question,pk=question_id)
    return render(request,'polls/detail.html',{'question':question})

'''
# Raising a 404 error
    try:
        question=Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not Exist")
    return render(request,'polls/detail.html',{'question':question})


    #return HttpResponse("You are looking at question %s." %question_id)
'''
def results(request,question_id):
    response="you are looking at results of %s."
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("You are voting on question %s ." % question_id)

