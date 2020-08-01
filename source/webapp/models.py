from django.db import models

DEFAULT_CATEGORY = ('active')
CATEGORY_CHOICES = (
    (DEFAULT_CATEGORY,'Активно'),
    ('blocked','Заблокировано')
)

class Guest(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(max_length=200, verbose_name='Почта' )
    text = models.TextField(max_length=1000, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.CharField(max_length=20, verbose_name='Статус', choices=CATEGORY_CHOICES, default=DEFAULT_CATEGORY)

    def __str__(self):
        return f'{self.name} - {self.email}'