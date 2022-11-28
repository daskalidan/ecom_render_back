"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.conf.urls.static import static
from django.conf import settings
from knitted_back import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # login/logout
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', views.log_out),
    # register
    # path('register/', views.RegisterView.as_view(), name='auth_register'),
     path('register/', views.register_my_user),
    # products
    path('allproducts/', views.all_products),
    path('createnewproduct/', views.Create_new_product.as_view()),
    path('deleteproduct/', views.delete_product),
    path('editproduct/<int:id>', views.edit_product.as_view()),
    # categories
    path('allcategories/', views.all_categories),
    path('createnewcategory/', views.create_new_category),
    path('deletecategory/', views.delete_category),
    # orders
    path('placeneworder/', views.place_an_order)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
