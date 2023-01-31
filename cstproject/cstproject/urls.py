"""cstproject URL Configuration

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
from django.urls import path , include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/page/2003/
    path('page/2003/',views.page_2003),
    # http://127.0.0.1:8000/page/2023/
    path('page/2023/',views.page_2023_view),

    path('page/2',views.page_2),
    path('page/3',views.page_3),

    path('',views.page_index),
    path('test_html',views.test_html),
    # http://12.0.0.1:8000/page/3-number

    path('page/<int:pg>', views.pagen_view),
    # http://127.0.0.1:8000/200/add/300
    path('<int:n>/<str:op>/<int:m>',views.cal_view),
    # http://127.0.0.1:8000/cst_index
    path('cst_index', views.cst_index),

    path('aboutus', views.aboutus_view),

    #http://127.0.0.1:8000/music/index
    path('music/',include('music.urls')),


]
