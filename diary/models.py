from django.db import models
from django.utils import timezone


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    created_at = models.DateTimeField('日付', default=timezone.now)
