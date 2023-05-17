from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('vacancies/', vacancies, name='vacancies'),
    path('goods/', goods, name='goods'),
    path('stock/', stock, name='stock'),
    path('vacancies/resume.html/', resume, name='resume'),
    path('goods/create_goods', create_goods, name='create_goods'),
    path('goods/edit_provider/<int:id>/', edit_provider, name='edit_provider'),
    path('goods/delete_provider/<int:id>/', delete_provider, name='delete_provider'),
    path('goods/edit_goods/<int:id>/', edit_goods, name='edit_goods'),
    path('goods/delete_goods/<int:id>/', delete_goods, name='delete_goods'),
    path('deal', deal, name='deal'),
    path('private_office/', private_office, name='private_office'),
    path('logout', logout_view, name='logout_view'),
    path('private_office/register', register, name='register')
]