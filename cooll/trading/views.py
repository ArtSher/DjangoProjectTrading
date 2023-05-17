from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


menu = [{'title': 'Главная ', 'url_name': 'home'},
        {'title': 'Контакты', 'url_name': 'contacts'},
        {'title': 'Вакансии', 'url_name': 'vacancies'},
        {'title': 'Товары и услуги', 'url_name': 'goods'},
        {'title': 'Склад', 'url_name': 'stock'},
        {'title': 'Личный кабинет', 'url_name': 'private_office'},
]


def index(request):
    return render(request, 'trading/index.html', {'title': 'Главная ', 'menu': menu})


def contacts(request):
    return render(request, 'trading/contacts.html', {'title': 'Контакты', 'menu': menu })


def vacancies(request):
    vacancy = Vacancies.objects.all()
    return render(request, 'trading/vacancies.html', {'vacancy': vacancy, 'title': 'Вакансии', 'menu': menu, })


def goods(request):
    if request.method == 'POST':
        providerForm = ProviderForm(request.POST)
        if providerForm.is_valid():
            companyName = providerForm.cleaned_data['companyName']
            provider = Provider(companyName=companyName)
            provider.save()
        else:
            print('Неверный формат данных')
        return redirect('goods')
    else:
        goods = Goods.objects.all()
        provider = Provider.objects.all()


        providerForm = ProviderForm()
        goodsForm = GoodsForm()

        data = {'title': 'Товары и услуги', 'menu': menu, 'goods': goods,
                'provider': provider, 'providerForm': ProviderForm, 'goodsForm': GoodsForm
                }
        return render(request, 'trading/goods.html', context=data)


def create_goods(request):
    if request.method == 'POST':
        goodsForm = GoodsForm(request.POST)
        if goodsForm.is_valid():
            nameGoods = goodsForm.cleaned_data['nameGoods']
            descriptionGoods = goodsForm.cleaned_data['descriptionGoods']
            goods = Goods(nameGoods=nameGoods, descriptionGoods=descriptionGoods)
            goods.save()
        else:
            print('Неверный формат данных')
        return redirect('goods')


def edit_provider(request, id):
    try:
        provider = Provider.objects.get(id=id)

        if request.method == "POST":
            providerForm = ProviderForm(request.POST)
            provider.companyName = request.POST.get('companyName')
            provider.save()
            return redirect('goods')
        else:
            return render(request, 'trading/edit.html', {'provider': provider, 'providerForm': ProviderForm})
    except Provider.DoesNotExist:
        return HttpResponseNotFound('Provider not found')


def delete_provider(request, id):
    try:
        provider = Provider.objects.get(id=id)
        provider.delete()
        return redirect('goods')
    except Provider.DoesNotExist:
        return HttpResponse('Invalid data')


def edit_goods(request, id):
    try:
        goods = Goods.objects.get(id=id)

        if request.method == "POST":
            goodsForm = GoodsForm(request.POST)
            goods.nameGoods = request.POST.get('nameGoods')
            goods.descriptionGoods = request.POST.get('descriptionGoods')
            goods.save()
            return redirect('goods')
        else:
            return render(request, 'trading/edit_goods.html', {'goods': goods, 'goodsForm': GoodsForm})
    except Provider.DoesNotExist:
        return HttpResponseNotFound('Provider not found')


def delete_goods(request, id):
    try:
        goods = Goods.objects.get(id=id)
        goods.delete()
        return redirect('goods')
    except Provider.DoesNotExist:
        return HttpResponse('Invalid data')


def stock(request):
    if request.method == 'POST':
        stockForm = StockForm(request.POST)
        if stockForm.is_valid():
            stockForm.save()
        else:
            print('Неверный формат данных')
        return redirect('stock')
    else:
        stock = Stock.objects.all()
        stockForm = StockForm()

        data = {'title': 'Склад', 'menu': menu,
                'stockForm': StockForm, 'stock': stock
               }
        return render(request, 'trading/stock.html', context=data)


def resume(request):
    if request.method == 'POST':
        userForm = UserForm(request.POST, request.FILES)
        if userForm.is_valid():
            userForm.name = request.POST.get("name")
            userForm.surname = request.POST.get("surname")
            userForm.age = request.POST.get("age")
            userForm.photo = request.POST.get("photo")
            userForm.email = request.POST.get("email")
            userForm.phon = request.POST.get("phon")
            userForm.save()
            return redirect('vacancies')
        else:
            return HttpResponse('Invalid data')
    else:
        userForm = UserForm()
    return render(request, 'trading/resume.html', {'form': userForm})


def deal(request):
    deals = Deal.objects.all()
    return render(request, 'trading/deal.html', {'deals': deals})


def private_office(request):
    if request.method == 'POST':
        userForm = LoginForm(request.POST)
        if userForm.is_valid():
            loginUser = userForm.cleaned_data['login']
            passwordUser = userForm.cleaned_data['password']
            print(loginUser, passwordUser)
            user = authenticate(username=loginUser, password=passwordUser)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('private_office')
        return redirect('home')
    loginForm = LoginForm()
    return render(request, 'trading/private_office.html', {'loginForm': loginForm, 'menu': menu})


def logout_view(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        userCreationForm = UserCreationForm(request.POST)
        if userCreationForm.is_valid():
            username = userCreationForm.cleaned_data['username']
            password = userCreationForm.cleaned_data['password1']
            User.objects.create_user(username=username, password=password)
            return redirect('private_office')
        else:
            return HttpResponse('Invalid data')
    userCreationForm = UserCreationForm()
    return render(request, 'trading/register.html', {'userCreationForm': UserCreationForm})