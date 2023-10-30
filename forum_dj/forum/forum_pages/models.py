from django.db import models
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     pass

class Advertisements(models.Model):
    title = models.CharField('Тайтл', max_length=50)
    text = models.TextField('Повідомлення')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Реклама'
        verbose_name_plural = 'Реклами'
