"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path, include

from bookmark.views import BookmarkListView

# path : 주소 접속시 어떤 뷰를 동작
# re_path : 어떤 주소(정규 표현식) 동작
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookmark/', include('bookmark.urls', namespace='bookmark')),
    path('',BookmarkListView.as_view(),name='index'),
]
