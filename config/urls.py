from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Redirige raíz a API
    path('', lambda request: redirect('/api/')),

    path('admin/', admin.site.urls),

    # 🔐 LOGIN JWT
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # APIs
    path('api/', include('api.urls')),
]