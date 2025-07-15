from django.urls import path, include, re_path
from django.views.generic import TemplateView

from .views import GetCSRFToken, RetrieveUpdateAPIView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/appAccess/<int:id>/', RetrieveUpdateAPIView.as_view()),
    path('csrf_cookie/', GetCSRFToken.as_view()),
]

# Final fallback: exclude all /auth/ routes
urlpatterns += [
    re_path(r'^(?!auth).*$', TemplateView.as_view(template_name="index.html")),
]
