"""
URL configuration for get_all_frogs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from forum.views import store_list, store_detail
#from api.views import CommentsList, CommentsByStore, CommentsByParent

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('authenti/', include('authenti.urls')),
    path('achievments/', include('achievments.urls')),
    path('pages/', include('pages.urls')),
    path('stores/', store_list, name='store-list'),
    path('stores/<int:store_id>/', store_detail, name='store-detail'),
    #----API----
    path('A/', include('api.urls')),
]
