from django import forms
from .models import CATEGORY_CHOICES

default_status = CATEGORY_CHOICES[0][0]


BROWSER_DATETIME_FORMAT = '%Y-%m-%dT%H:%M'


class GuestForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Имя')
    email = forms.EmailField(max_length=200, required=True, label='Почта')
    text = forms.CharField(max_length=2000, required=True, label='Текст')
    status = forms.ChoiceField(choices=CATEGORY_CHOICES, initial=default_status, label='Статус')
    created_at = forms.DateTimeField(required=False, label='Время публикации',
                                     input_formats=['%Y-%m-%d', BROWSER_DATETIME_FORMAT,
                                                    '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M',
                                                    '%Y-%m-%d %H:%M:%S'],
                                     widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))