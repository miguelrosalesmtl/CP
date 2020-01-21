"""shopping_cart URL Configuration

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
from rest_framework_nested import routers
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    FoodAPIView,
    OrderLDRViewSet,
    OrderDetailCDViewSet)

router = routers.SimpleRouter()
router.register(r'orders', OrderLDRViewSet)

order_details_router = routers.NestedSimpleRouter(router, r'orders', lookup='orders')
order_details_router.register(r'details', OrderDetailCDViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Shopping Cart API",
      default_version='v1',
      description="Shopping Cart API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="miguel.f.rosales@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/food/', FoodAPIView.as_view()),
    path('api/purchases/', include(router.urls)),
    path('api/purchases/', include(order_details_router.urls)),
]
