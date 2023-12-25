from django.urls import path
from myapp.views import index,contacts,indexItem
app_name = 'myapp'

urlpatterns =[
    path('', index),
    path('<int:id>/', indexItem, name='detail' ),
    path('contacts/', contacts),

 ]