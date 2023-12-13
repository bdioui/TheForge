from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Main'
urlpatterns = [
    path('', views.Index, name='index'),
    path('about/', views.About, name='about'),
    path('join/', views.Join, name='join'),
    path('contact/', views.Contact, name='contact'),
    path('ai/', views.AI, name='ai'),
    path('cyber/', views.Cyber, name='cyber'),
    path('iot/', views.IoT, name='iot'),

    path('blog/', views.Blog, name='blog'),
    path('create_post/', views.Create_Post, name='create_post'),
    path('post/<int:pk>', views.Post_detail, name='post'),

    path('create_job/', views.Create_Job, name='create_job'),
    path('job/<int:pk>', views.Job_Detail, name='job'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)