"""e_commerce URL Configuration

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
from .views import home_page, about_page, contact_page, login_page, register_page, logout_page
from django.conf import settings
from django.conf.urls.static import static
from products.views import ProductDetailView, ProductFeaturedListView, ProductFeaturedDetailView, ProductDeleteView
from django.views.generic import TemplateView
from carts.views import cart_home
from products.views import ProductCreatView
                            
urlpatterns = [
        path('', home_page, name='home'),
        path('about/', about_page, name='about'),
	    path('contact/', contact_page, name='contact'),
        path('cart/', cart_home, name='cart'),
        path('login/', login_page, name='login'),
        path('logout/', logout_page, name='logout'),
        path('register/', register_page, name='register'),
        path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
        path('products/create/', ProductCreatView.as_view(), name ='creat'),
        path('products/<int:pk>', ProductDetailView.as_view()),
        path('admin/', admin.site.urls),
        path('featured/', ProductFeaturedListView.as_view()),
        path('featured/<int:pk>/', ProductFeaturedDetailView.as_view()),
        path('products/<slug:slug>/', ProductDeleteView.as_view(), name = 'delete-view'),
        path('products/', include("products.urls", namespace="products")),
        path('search/', include("search.urls", namespace="search")),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
