from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apps import UsersConfig
from .views import UsersViewSet


app_name = UsersConfig.name
router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls), name='users'),
    path('', include('djoser.urls.authtoken'))
]
