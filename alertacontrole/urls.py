from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf.urls.static import static

from app.views import home, registros, store, painel, dologin, dashboard, logouts, logout_view

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    # note the override comes before the admin URLs below
    path('admin/logout/', lambda request: redirect('/logout/', permanent=False)),
    path('admin/', admin.site.urls),
    path('', home),
    path('registros/', registros),
    path('store/', store),
    path('painel/', painel),
    path('dologin/', dologin),
    path('dashboard/', dashboard),
    path('logouts/', logouts),
]

admin.AdminSite.site_header = 'Controle Alerta Serviços'
admin.AdminSite.site_title = 'Controle de Veículos ALERTA'
admin.AdminSite.index_title = 'ALERTA SERVIÇOS'