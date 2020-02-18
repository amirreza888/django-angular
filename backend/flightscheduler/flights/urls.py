from django.urls import path
from . import views
from rest_framework import routers
from django.conf.urls import include

router = routers.DefaultRouter()
router.register(r'whatever', views.UserViewSet)

urlpatterns = [
    #path('',views.index,name='index'),
    path('',include(router.urls))
]