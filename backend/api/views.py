from rest_framework import viewsets, generics
from django.contrib.auth.models import User
from .models import NewsEvent, Tender, Partner, Faculty, ProfessionalCourse
from .serializers import (
    NewsEventSerializer, TenderSerializer, PartnerSerializer,
    FacultySerializer, ProfessionalCourseSerializer, RegisterSerializer
)

class NewsEventViewSet(viewsets.ModelViewSet):
    queryset = NewsEvent.objects.all().order_by('-date')
    serializer_class = NewsEventSerializer

class TenderViewSet(viewsets.ModelViewSet):
    queryset = Tender.objects.all().order_by('-date_posted')
    serializer_class = TenderSerializer

class PartnerViewSet(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

class ProfessionalCourseViewSet(viewsets.ModelViewSet):
    queryset = ProfessionalCourse.objects.all()
    serializer_class = ProfessionalCourseSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
