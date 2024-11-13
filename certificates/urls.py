from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CertificateCreateView, CertificateVerificationView, CertificateSoftDeleteView, CertificateRestoreView

router = DefaultRouter()
router.register(r'create', CertificateCreateView)

urlpatterns = [
    path('', include(router.urls)),
    path('verify/', CertificateVerificationView.as_view(), name='verify_certificate'),
    path('<str:certificate_id>/delete/', CertificateSoftDeleteView.as_view(), name='soft_delete_certificate'),
    path('<str:certificate_id>/restore/', CertificateRestoreView.as_view(), name='restore_certificate'),
]