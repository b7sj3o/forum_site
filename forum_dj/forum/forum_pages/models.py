from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100,
                                null=True,
                                unique=True,
                                verbose_name='Ваш нікнейм')
   
    email = models.EmailField(null=True,
                              unique=True,
                              verbose_name='Ваш E-mail')
   
    telegram = models.CharField(max_length=200,
                                null=True, 
                                blank=True, 
                                verbose_name='Ваш телеграм нікнейм')
   
    is_show_telegram = models.BooleanField(default=True, 
                                           verbose_name='Показувати телеграм')
   
    avatar = models.ImageField(null=True, 
                               default='forum_pages/img/avatars/default_avatar.png',
                               upload_to='forum_pages/img/avatars', 
                               verbose_name='Фото профілю')

    is_blocked = models.BooleanField(default=False, blank=True)
    ban_reason = models.TextField(null=True, blank=True)

    REQUIRED_FIELDS = []


class Advertisements(models.Model):
    title = models.CharField('Тайтл', max_length=50)
    text = models.TextField('Повідомлення')
    name = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    time = models.DateTimeField('Час', auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title} - {self.name}"

    class Meta:
        verbose_name = 'Оголошення'
        verbose_name_plural = 'Оголошення'


class MainTextBanner(models.Model):
    title = models.CharField('Тайтл', max_length=100)
    text = models.TextField('Повідомлення')
    detailed_text = models.TextField('Детальний опис')
    image = models.ImageField('Фото', upload_to='forum_pages/img/banners')
    link = models.URLField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Головний текст зверху'
        verbose_name_plural = 'Головний текст зверху'


class MainPictureBanner(models.Model):
    title = models.CharField('Тайтл', max_length=100)
    detailed_text = models.TextField('Детальний опис')
    image = models.ImageField('Фото', upload_to='forum_pages/img/banners')
    link = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Головний банер зверху'
        verbose_name_plural = 'Головний банер зверху'


class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    main_text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


class Themes(models.Model):
    title = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.title


class SubThemes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    base_theme = models.ForeignKey(
        Themes, on_delete=models.CASCADE, null=True, related_name='subthemes')
    title = models.CharField(max_length=100, null=True)
    main_text = models.TextField()
    count = models.PositiveIntegerField(default=0)
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


class SubThemeMessage(BaseMessage):
    subtheme = models.ForeignKey(
        SubThemes, on_delete=models.CASCADE, null=True, related_name='subtheme_messages')


class SandboxMessage(BaseMessage):
    pass


class TopAgency(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='forum_pages/img/top_agency')
    detailed_text = models.TextField('Детальний опис')
    link = models.URLField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class BaseTheme(models.Model):
    assoc = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()

    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.assoc}, {self.user}"
