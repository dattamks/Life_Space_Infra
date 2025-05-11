from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus/',views.aboutus,name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog_details/', views.blog_details, name='blog_details'),
    path('contact/', views.contact, name='contact'),
    path('elements/', views.elements, name='elements'),
    path('gallery/', views.gallery, name='gallery'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='work'),
       
]
