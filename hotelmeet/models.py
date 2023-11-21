from django.db import models
from accounts.models import CustomUser
# Create your models here.

class RoomPost(models.Model):

    user=models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE
    )

    address=models.CharField(
        verbose_name='住所',
        max_length=200
    )

    image=models.ImageField(
        verbose_name='写真',
        upload_to='photos'
    )
    
    price=models.IntegerField(
        verbose_name='価格'
    )

    posted_at=models.DateTimeField(
        verbose_name='投稿日時',
        auto_now_add=True
    )
    
    def __str__(self):
      return self.address