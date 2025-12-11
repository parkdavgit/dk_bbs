from django.contrib import admin
#from django.conf.urls import url
from django.urls import path, re_path
from bbbs1 import views 
 
 
urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^board/(?P<question_id>\d+)/$', views.question_detail, name='question_detail'), ## 추가 ##
    re_path(r'^board/question_create/$', views.question_create, name='question_create'), ## 추가 ##
    re_path(r'^board/answer_create/(?P<question_id>\d+)/$', views.answer_create, name='answer_create'),
    re_path(r'^board/question_modify/(?P<question_id>\d+)/$', views.question_modify, name='question_modify'),
    re_path(r'^board/question_delete/(?P<question_id>\d+)/$', views.question_delete, name='question_delete'),
    #url(r'^board/answer_modify/(?P<answer_id>\d+)/$', views.answer_modify, name='answer_modify'),
    #url(r'^boards/answer_delete/(?P<answer_id>\d+)/$', views.answer_delete, name='answer_delete'),
    re_path(r'^vote/question/(?P<question_id>\d+)/$', views.vote_question, name='vote_question'),
    #url(r'^vote/answer/(?P<answer_id>\d+)/$', views.vote_answer, name='vote_answer'),
    re_path(r'^user_search/$', views.user_search, name='user_search'), 
    re_path(r'^profile/$', views.profile, name='profile'), 
    


     
] 