from rest_framework import serializers
from django.contrib.auth.models import User
from .models import NewsEvent, NewsImage, Tender, Partner, Faculty, FacultyOption, ProfessionalCourse

class NewsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = ['id', 'image']

class NewsEventSerializer(serializers.ModelSerializer):
    images = NewsImageSerializer(many=True, read_only=True)

    class Meta:
        model = NewsEvent
        fields = ['id', 'title_en', 'title_fr', 'date', 'description_en', 'description_fr', 'category', 'created_at', 'images']

class TenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tender
        fields = ['id', 'title_en', 'title_fr', 'description_en', 'description_fr', 'file', 'date_posted', 'deadline']

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'name_en', 'name_fr', 'country_en', 'country_fr', 'type', 'logo']

class FacultyOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyOption
        fields = ['id', 'name_en', 'name_fr']

class FacultySerializer(serializers.ModelSerializer):
    options = FacultyOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Faculty
        fields = ['id', 'name_en', 'name_fr', 'icon_name', 'options']

class ProfessionalCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalCourse
        fields = ['id', 'name_en', 'name_fr', 'icon_name']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user
