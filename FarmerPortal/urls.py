"""FarmerPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from Portal import views as my_views
from users import views as users_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Portal.urls')),

    path('profile/',my_views.profile,name="profile"),
    path('cart/',my_views.cart,name="cart"),

    path('search/',my_views.search,name="search"),
    path('seller_rating/<int:pk>',my_views.seller_rating,name="seller_rating"),
    path('seller_rating2',my_views.seller_rating2,name="seller_rating2"),

    path('cart/<int:id>/',my_views.cart,name="cart_update"),
    path('order/',my_views.order,name="order"),
    path('cancel/<int:id>/',my_views.cancel,name="cancel"),
    path('farmerorder/',my_views.farmerorder,name="farmerorder"),
    path('farmerproducts/',my_views.farmerproducts,name="farmerproducts"),
    path('farmerproducts/<int:id>/',my_views.farmerproducts,name="farmerproducts_update"),
    path('delprod/<int:id>/',my_views.delprod,name="delprod"),

    path('signup/',users_views.signup,name="signup"),
    path('login/',auth_views.LoginView.as_view(template_name="users/login.html"),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name="Portal/index.html"),name="logout"),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),name="password_reset"),
    path('password_reset_sent/',auth_views.PasswordResetDoneView.as_view(template_name="users/password_rest_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"),name="password_reset_confirm"),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),name="password_reset_complete"),

    path('about/',my_views.about,name="about"),
    path('contact/',my_views.contact,name="contact"),

    path('photos/',include("photos.urls")),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
