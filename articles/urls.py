from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'articles'

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name='create'),
    path('delete/<int:artId>', views.delete, name='delete'),
    path('update/<int:artId>', views.update, name='update'),
    path('header/', views.header, name='header'),
    path('footer/', views.footer, name='footer'),
    path('bsell_profile/', views.bsell_profile, name='bsell_profile'),
    path('del_bprofile/<int:profId>', views.del_bprofile, name='del_bprofile'),
    path('del_bprofile/<int:profId>', views.del_bprofile, name='up_bprofile'),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
