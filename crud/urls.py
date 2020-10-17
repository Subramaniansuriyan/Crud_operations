from django.urls import path
from .import views

urlpatterns=[
    path('create',views.add_member,name='add_member'),
    path('all',views.list_member,name='list_member'),
    path('update',views.edit_member,name='edit_member'),
    path('delete',views.delete_member,name='delete_member')
]