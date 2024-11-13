from django.urls import path, include

from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView
)


urlpatterns = [

    path('api/users/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


    path('api/accounts/auth/', include('users.urls')), 
    path('api/certificates/', include('certificates.urls')),
    path('api/analytics/', include('analytics.urls')),
    path('admin/', admin.site.urls),
]