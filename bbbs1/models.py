#from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User 


class Question(models.Model):
    subject = models.CharField(max_length=100)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question') ## 수정 ##
    voter = models.ManyToManyField(User, related_name='voter_question')  ## 추가 ##
 
    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 추가
    modify_at = models.DateTimeField(null=True, blank=True) #추가
    #voter = models.ManyToManyField(User, related_name='voter_answer')

    def __str__(self):
        return self.content          