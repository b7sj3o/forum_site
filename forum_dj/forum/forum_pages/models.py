from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Advertisements(models.Model):
    title = models.CharField('Тайтл', max_length=50)
    text = models.TextField('Повідомлення')
    time = models.DateTimeField('Час', auto_now_add=True)
    name = models.TextField('Нік користувача')


    def __str__(self) -> str:
        return f"{self.title} - {self.name}"
    
    class Meta:
        verbose_name = 'Реклама'
        verbose_name_plural = 'Реклами'

class MainTextBanner(models.Model):
    title = models.CharField('Тайтл', max_length=100)
    text = models.TextField('Повідомлення')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Вибраний продукт'
        verbose_name_plural = 'Вибрані продукти'

class MainPictureBanner(models.Model):
    image = models.ImageField('Фото', upload_to='')

    class Meta:
        verbose_name = 'Головний банер'
        verbose_name_plural = 'Головні банери'


class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    main_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Themes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=True)
    main_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
    

class BaseMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    main_text = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.main_text[0:500]

    # dont create a table in DB
    class Meta:
        abstract = True 

class ThemeMessage(BaseMessage):
    theme = models.ForeignKey(Themes, on_delete=models.CASCADE, null=True)

class SandboxMessage(BaseMessage):
    pass
