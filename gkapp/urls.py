from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:produto_id>', views.produto, name='produto')
]
