"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from libraryapp import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login),
    #url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
    #url(r'^logout/$', auth_views.logout),
    url('index/',views.user_register),
    url('addbook/',views.addingbooks),
    url('sucess/',views.sucess),
    url('welcome/',views.welcome),
    url('logincheck',views.login_check),
    url('^Add/(?P<book_id>\d+)/(?P<book_name>\w+)/(?P<book_publisher>\w+)/(?P<req_user>\w+)/$', views.Add),
    url('view_book/', views.viewbooks),
    url('^returned/(?P<id>\d+)/$', views.returned),
    url('query/', views.user_querying),
    url('logout/', views.logout_view),
]
