from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='blog-about'),
    path('rent/', views.rent, name='blog-rent'),
    path('add_item/', views.add_item, name='add_item'),
    path('remove_item/<int:item_id>/', views.remove_item, name='remove_item'),
    path('edit_item/<int:item_id>/', views.edit_item, name='edit_item'),
    path('item_list/', views.item_list, name='item_list'),
    path('category/<int:category_id>/', views.category_list, name='category-list'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('rent_item/<int:item_id>/', views.rent_item, name='rent_item'),
]