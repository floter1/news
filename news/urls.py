"""news URL Configuration 
 
The `urlpatterns` list routes URLs to views. For more information please see: 
    https://docs.djangoproject.com/en/2.1/topics/http/urls/ 
Examples: 
Function views 
    1. Add an import:  from my_app import views 
    2. Add a URL to urlpatterns:  path('', views.home, name='home') 
Class-based views 
    1. Add an import:  from other_app.views import Home 
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home') 
Including another URLconf 
    1. Import the include() function: from django.urls import include, path 
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')) 
""" 
from django.contrib import admin 
from django.urls import path, include, re_path 
from django.conf.urls.static import static
from django.conf import settings

#Wagtail
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('home/', include('articles.urls')), 
    path('users_home/', include('members.urls')),
    path('avatar/', include('avatar.urls')),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  





