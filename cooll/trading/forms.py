from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = ResumeUser
        fields = ['name', 'surname', 'age', 'photo', 'email', 'phon', 'is_published']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя'}),
            'surname': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Фамилия'}),
            'age': forms.TextInput(attrs={'class': 'form-input', 'type': 'number', 'placeholder': 'Возраст'}),
            'email': forms.TextInput(attrs={'class': 'form-input', 'type': 'email', 'placeholder': 'Эл. Почта'}),
            'phon': forms.TextInput(attrs={'class': 'form-input', 'type': 'number', 'placeholder': 'Телефон'})
        }
        labels = {
            'name': 'Имя', 'surname': 'Фамилия', 'age': 'Возраст', 'photo': ' Фото',
            'email': 'Эл. Почта', 'phon': 'Телефон', 'is_published': 'Публикация'
        }


class ProviderForm(forms.Form):
    companyName = forms.CharField(label='Поставщик')


class GoodsForm(forms.Form):
    nameGoods = forms.CharField(label='Наименование товара')
    descriptionGoods = forms.CharField(label='Описание товара')


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['goods', 'provider',  'price', 'quantityGoods', 'time_create']
        labels = {'goods': 'Товары', 'provider': 'Поставщик',
                  'price': 'Цена', 'quantityGoods': 'Количетсво товара',
                  'time_create': 'Дата создания'
                  }
        widgets = {
            'goods': forms.Select(attrs={'placeholder': 'Товары', 'style': 'max-width: 350px;'}),
            'provider': forms.Select(attrs={'placeholder': 'Поставщик', 'style': 'max-width: 350px;'}),
            'time_create': forms.DateInput(attrs={'placeholder': 'Дата поставки', 'type': 'date', 'style': 'max-width: 300px;'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Цена', 'style': 'max-width: 300px;'}),
            'quantityGoods': forms.NumberInput(attrs={'placeholder': 'Количество', 'style': 'max-width: 300px;'}),
        }


class LoginForm(forms.Form):
    login = forms.CharField(max_length=20, label='Логин', widget=forms.TextInput(attrs={'placeholder': 'Логин', 'class': 'loginForm'}))
    password = forms.CharField(max_length=20, label='Пароль', widget=forms.TextInput(attrs={'type': 'password', 'placeholder': 'Пароль', 'class': 'loginForm'}))