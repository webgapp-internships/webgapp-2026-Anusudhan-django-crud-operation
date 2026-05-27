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
    path('formedit/<int:id>',views.formedit,name='formedit'),
    path('formdelete/<int:id>',views.formdelete,name='formdelete')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT);
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)