from django.db import models
from django.utils import timezone

class Advertisements(models.Model):
    title = models.CharField('Тайтл', max_length=50)
    text = models.TextField('Повідомлення')
    time = models.DateTimeField('Час', auto_now_add=True)
    name = models.TextField('Нік користувача')


    def __str__(self):
        return f"{self.title} - {self.name}"
    
    class Meta:
        verbose_name = 'Реклама'
        verbose_name_plural = 'Реклами'

class ChosenProduct(models.Model):
    title = models.CharField('Тайтл', max_length=100)
    text = models.TextField('Повідомлення')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Вибраний продукт'
        verbose_name_plural = 'Вибрані продукти'

class MainBanner(models.Model):
    image = models.ImageField('Фото', upload_to='')

    class Meta:
        verbose_name = 'Головний банер'
        verbose_name_plural = 'Головні банери'

