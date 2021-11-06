from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=30)  # 문자열의 최대길이 30으로 지정
    content = models.TextField()  # 문자열의 길이 제한이 없음

    created_at = models.DateTimeField(auto_now_add=True)  # 월, 일, 시, 분, 초 기록
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}] {self.title}'
