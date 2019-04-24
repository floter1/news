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
    path('del_bprofile/<int:profId>', views.del_bprofile, name='del_bprofile'),
    path('up_bprofile/<int:profId>', views.up_bprofile, name='up_bprofile'),
    path('bprofile/', views.bsell_profile, name='bsell_profile'),
    path('sell_friends/', views.sell_friends, name='sell_friends'),
    path('buy_friend/<int:fsellId>', views.buy_friend, name='buy_friend'),
    path('avatar/', include('avatar.urls')),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
