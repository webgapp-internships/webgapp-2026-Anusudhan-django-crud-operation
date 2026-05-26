from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('flex',views.flex,name='flex'),
    path('form',views.form,name='form'),
    path('formresult',views.formresult,name='formresult'),
    path('formedit',views.formedit,name='formedit'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT);