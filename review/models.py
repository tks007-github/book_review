from accounts.models import CustomUser
from django.db import models

# Create your models here.

EVALUATION_CHOICES = [('☆☆☆', '☆☆☆：良い'), ('☆☆', '☆☆　：普通'), ('☆', '☆　　：悪い')]
class Review(models.Model):
    """レビューモデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='内容')
    photo = models.ImageField(verbose_name='写真', blank=True, null=True)
    useful_review = models.IntegerField(verbose_name='いいね', null=True, blank=True, default=0)
    review = models.TextField(verbose_name='講評')
    evaluation = models.CharField(verbose_name='評価', max_length=10, choices=EVALUATION_CHOICES)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Review'

        def __str__(self):
            return self.title
