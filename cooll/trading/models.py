from django.db import models
from django.contrib.auth.models import User


class Vacancies(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


    def __str__(self):
        return self.title


class ResumeUser(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    surname = models.CharField(max_length=50, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Прикрепить фотографию')
    email = models.EmailField(verbose_name='Эл. почта')
    phon = models.IntegerField(verbose_name='Контактный номер')
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Goods(models.Model):
    nameGoods = models.CharField(max_length=70)
    descriptionGoods = models.TextField()

    def __str__(self):
        return self.nameGoods


class Provider(models.Model):
    companyName = models.CharField(max_length=200)

    def __str__(self):
        return self.companyName


class Stock(models.Model):
    goods = models.ForeignKey('Goods', on_delete=models.CASCADE)
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    time_create = models.DateField()
    time_update = models.DateTimeField(auto_now=True)
    price = models.IntegerField()
    quantityGoods = models.IntegerField()


class Deal(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    time_create = models.DateField()
    price = models.IntegerField()
    quantityGoods = models.IntegerField()

    def __str__(self):
        return str(self.goods) + '' + str(self.price)
