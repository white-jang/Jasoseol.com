from django.db import models
from django.contrib.auth.models import User

# 자소서 
class Jasoseol(models.Model):
    title = models.CharField(max_length=50) # 제목
    content = models.TextField() # 내용
    updated_at = models.DateTimeField(auto_now=True) # (auto_now=True) : 현재 시간을 자동으로 저장
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # 작성자
    # 외래키로 연결된 object가 지워질 때 같이 지워진다
    # = 유저가 없어지면 유저가 작성한 자소설도 없어진다

# 댓글
class Comment(models.Model):
    content = models.CharField(max_length=100) # 내용
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # 작성자
    jasoseol = models.ForeignKey(Jasoseol, on_delete=models.CASCADE) # 댓글이 달린 자소서