from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'api'
router = DefaultRouter()
router.register(r'info', views.InfoViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]