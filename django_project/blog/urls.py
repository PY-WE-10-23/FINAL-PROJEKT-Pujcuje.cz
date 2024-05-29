from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('rent/', views.rent, name='blog-rent'),
    path('add_item/<int:item_id>/', views.add_item, name='add_item'),
    path('remove_item/<int:item_id>/', views.remove_item, name='remove_item'),
    path('edit_item/<int:item_id>/', views.edit_item, name='edit_item'),
    path('category/<int:category_id>/', views.category_list, name='category-list')

]