from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=100, null=True, unique=True, verbose_name='Ваш нікнейм')
    email = models.EmailField(null=True, unique=True, verbose_name='Ваш E-mail')
    telegram = models.CharField(max_length=200, null=True, blank=True, verbose_name='Ваш телеграм нікнейм')  
    is_show_telegram = models.BooleanField(default=True, verbose_name='Показувати телеграм')
    avatar = models.ImageField(null=True, default='forum_pages/img/avatars/default_avatar.png', upload_to='forum_pages/img/avatars', verbose_name='Фото профілю')


    REQUIRED_FIELDS = []

class Advertisements(models.Model):
    title = models.CharField('Тайтл', max_length=50)
    text = models.TextField('Повідомлення')
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    time = models.DateTimeField('Час', auto_now_add=True)


    def __str__(self) -> str:
        return f"{self.title} - {self.name}"
    
    class Meta:
        verbose_name = 'Оголошення'
        verbose_name_plural = 'Оголошення'

class MainTextBanner(models.Model):
    title = models.CharField('Тайтл', max_length=100)
    text = models.TextField('Повідомлення')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Головний текст зверху'
        verbose_name_plural = 'Головний текст зверху'

class MainPictureBanner(models.Model):
    image = models.ImageField('Фото', upload_to='forum_pages/img/banners')

    class Meta:
        verbose_name = 'Головний банер зверху'
        verbose_name_plural = 'Головний банер зверху'

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
