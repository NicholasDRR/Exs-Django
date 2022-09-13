from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('admin', admin, name='admin'),
    path('contato', contato, name='contato'),
    path('produto/<int:id>', produto, name='produto'),
]
