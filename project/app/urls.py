from django.urls import include, path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers 
from .views import *
from rest_framework.authtoken import views

# define the router
router = routers.DefaultRouter()
router.register(r'movie', MovieViewSet)
router.register(r'student', StudentViewSet)
  
# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]