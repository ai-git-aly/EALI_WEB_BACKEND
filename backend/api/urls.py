from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    NewsEventViewSet, TenderViewSet, PartnerViewSet,
    FacultyViewSet, ProfessionalCourseViewSet, RegisterView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'news', NewsEventViewSet)
router.register(r'tenders', TenderViewSet)
router.register(r'partners', PartnerViewSet)
router.register(r'faculties', FacultyViewSet)
router.register(r'courses', ProfessionalCourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
