from django.urls import path
from .import views


urlpatterns = [
    path('', views.home,name='index'),
    path('about/', views.about,name='about'),
    path('services/', views.services,name='service'),
    path('events/', views.events,name='event'),
    path('contact/', views.contact,name='contact'),
    path('send_sms/', views.send_sms, name='send_sms'),
    path('news/<int:blog_id>/', views.news_detail,name='detail'),

]
