"""pxweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from MyUsers.views import UserViewSet
from goods.views import GoodsViewSet
from myapp.views import index
from rest_framework.documentation import include_docs_urls
from django.views.static import serve
from pxweb.settings import MEDIA_ROOT
from rest_framework_jwt.views import obtain_jwt_token
import xadmin

API_TITLE = 'pxweb api documentation'
API_DESCRIPTION = 'pxweb api server for pxwebinfo'




# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'goods', GoodsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    path('', index),
    path('api/docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION, authentication_classes=[], permission_classes=[])),
    path('ueditor/', include('DjangoUeditor3.DjangoUeditor.urls')),
    #文件
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    path('jwt-auth/', obtain_jwt_token ),
    #path('api/goods/',GoodsListView.as_view(),name='goods-list'),
    #path('api/users/',UserViewSet.as_view(),name='users-list'),
]
