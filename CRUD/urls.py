"""CRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from crudapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Booklistview.as_view(),name='Home'),
    path('<int:pk>', views.Bookdetailview.as_view() ,name = 'Book-detail'),
    path('Create/', views.Bookcreateview.as_view()),
    path('Update/<int:pk>', views.BookUpdateview.as_view() ),
    path('delete/<int:pk>', views.BookDeleteview.as_view() ),
]
