from django.urls import path, include
from rest_framework import routers
from .views import GroupView, CategoryView

router = routers.DefaultRouter()
router.register('groups',GroupView)
router.register('categories',CategoryView)

urlpatterns = [
    path('',include(router.urls)),
]