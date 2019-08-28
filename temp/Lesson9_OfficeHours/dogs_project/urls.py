from django.conf.urls import url
from . import views


app_name = 'dogs_project'


urlpatterns = [
url(r'^$', views.index, name='index'),

url('new_dogname/', views.new_dogname, name='new_dogname'),
]

