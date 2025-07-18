from django.contrib import admin
from django.conf.urls import url
from bbbs1 import views 
 
 
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^board/(?P<question_id>\d+)/$', views.question_detail, name='question_detail'), ## 추가 ##
    url(r'^board/question_create/$', views.question_create, name='question_create'), ## 추가 ##
    url(r'^board/answer_create/(?P<question_id>\d+)/$', views.answer_create, name='answer_create'),
    url(r'^board/question_modify/(?P<question_id>\d+)/$', views.question_modify, name='question_modify'),
    url(r'^board/question_delete/(?P<question_id>\d+)/$', views.question_delete, name='question_delete'),
    #url(r'^board/answer_modify/(?P<answer_id>\d+)/$', views.answer_modify, name='answer_modify'),
    #url(r'^boards/answer_delete/(?P<answer_id>\d+)/$', views.answer_delete, name='answer_delete'),
    url(r'^vote/question/(?P<question_id>\d+)/$', views.vote_question, name='vote_question'),
    #url(r'^vote/answer/(?P<answer_id>\d+)/$', views.vote_answer, name='vote_answer'),
    url(r'^user_search/$', views.user_search, name='user_search'), 
    url(r'^profile/$', views.profile, name='profile'), 
    


     
] 