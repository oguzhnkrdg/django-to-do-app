from django.urls import path
from .views import GorevList, GorevDetay, GorevEkle, GorevGuncelle, GorevSil, GirisYap, KayitOl
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('giris/', GirisYap.as_view(), name='giris'),
    path('cikis/', LogoutView.as_view(next_page='giris'), name='cikis'),
    path('kayit/', KayitOl.as_view(), name='kayit'),
    path('', GorevList.as_view(), name='gorevler'),
    path('gorev/<int:pk>/', GorevDetay.as_view(), name='gorev'),
    path('gorev-ekle/', GorevEkle.as_view(), name='gorev-ekle'),
    path('gorev-guncelle/<int:pk>/', GorevGuncelle.as_view(), name='gorev-guncelle'),
    path('gorev-sil/<int:pk>/', GorevSil.as_view(), name='gorev-sil'),


]
