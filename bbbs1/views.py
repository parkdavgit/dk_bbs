from django.shortcuts import get_object_or_404, render, redirect ## 추가된 부분
from .models import Question ## 추가된 부분
from django.utils import timezone
from .forms import NewQuestionForm, AnswerForm 
from django.core.paginator import Paginator 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request): 
    question_list = Question.objects.order_by('-create_at') 
    # 입력 파라미터
    page = request.GET.get('page','1')
     
    # 페이징처리
    paginator = Paginator(question_list, 7)
    page_obj = paginator.get_page(page)
    return render(request, 'home.html',{'question_list':page_obj})

     
     

def question_create(request):
    if request.method == 'POST':
        form = NewQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_at = timezone.now()

            question.author = request.user         ### 추가 ####

            question.save()
            return redirect('home')
    else:
        form = NewQuestionForm()
    return render(request, 'question_create.html', {'form':form})

def question_detail(request, question_id):
    question = get_object_or_404(Question,id=question_id)
    return render(request, 'view_question.html', {'question':question}) 

@login_required(login_url='login')
def question_modify(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('question_detail', question_id=question_id)

    if request.method == 'POST':#form 채워 온 것을 받고  save 하고 나머지 author ,timezone 정해줌
        form = NewQuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_at = timezone.now()
            question.save()
            return redirect('question_detail', question_id=question_id)
    else:
        form = NewQuestionForm(instance=question)#question_create,html form에 question instance 넣어 보여줘라
        return render(request, 'question_create.html', {'form': form})


@login_required(login_url='login')
def question_delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('question_detail', question_id=question_id)
    question.delete()
    return redirect('home') 


def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.create_at = timezone.now()

            answer.author = request.user         ### 추가 ####
 
            answer.save()
            return redirect('question_detail',question_id=question_id)  

    else:
        form = AnswerForm()
    context = {'question':question,'form':form}
    return render(request, 'view_question.html',context) 

def vote_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, '자신이 작성한 글에는 추천할 수 없습니다.')
    else:
        question.voter.add(request.user)
    return redirect('question_detail', question_id=question_id) 


@login_required()
def user_search(request):

    subject = request.POST.get('subject', '').strip()
    
    polls = Question.objects.filter(subject=subject)
     
    page = request.GET.get('page','1')
    paginator = Paginator(polls, 4)
    polls = paginator.get_page(page)
    return render(request, 'home.html',{'question_list':polls})  


def profile(request):
     
     
    
    context = {'user': request.user}
    return render(request, 'profile.html', context)                                                   
