from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='fjb'),
    path('<int:jualan_id>', views.jualan, name='jualan'),
    path('<search>', views.jualan, name='search'),
]