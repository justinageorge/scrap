"""
URL configuration for scrapapplication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from scrapapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("scraps/all",views.ScrapListView.as_view(),name="scrap-all"),
    path("scraps/<int:pk>",views.ScrapDetailView.as_view(),name="scrap-detail"),
    path("scraps/<int:pk>/remove",views.ScrapDeleteView.as_view(),name="scrap-remove"),
    path("scraps/add",views.ScrapCreateView.as_view(),name="scrap-add"),
    path("scraps/<int:pk>/change",views.ScrapUpdateView.as_view(),name="scrap-change"),
    path("register",views.SignUpView.as_view(),name="register"),
    path("",views.SignInView.as_view(),name="signin"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
