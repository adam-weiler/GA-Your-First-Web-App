"""my_first_web_app URL Configuration

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

from django.urls import path
from my_first_web_app.views import root, gallery, home_page, portfolio, about_me, favourites

urlpatterns = [
    path('', root), #Redirect
    path('gallery/', gallery), #Redirect
    path('home/', home_page), #Page
    path('portfolio/', portfolio), #Page
    path('about_me/', about_me), #Page
    path('favourites/', favourites), #Page
]
