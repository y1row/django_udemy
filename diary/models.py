from django.db import models


class Diary(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField('タイトル', max_length=200)
    text = models.TextField('本文')
    created_at = models.DateTimeField('登録日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    class Meta:
        verbose_name = '日記'
        verbose_name_plural = '日記'
