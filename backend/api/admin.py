from django.contrib import admin
from .models import NewsEvent, NewsImage, Tender, Partner, Faculty, FacultyOption, ProfessionalCourse

class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1

@admin.register(NewsEvent)
class NewsEventAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'title_fr', 'date', 'category', 'created_at')
    list_filter = ('category', 'date')
    search_fields = ('title_en', 'title_fr', 'description_en', 'description_fr')
    inlines = [NewsImageInline]

@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    list_display = ('title_en', 'title_fr', 'date_posted', 'deadline')
    search_fields = ('title_en', 'title_fr', 'description_en', 'description_fr')

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_fr', 'country_en', 'country_fr', 'type')
    list_filter = ('type', 'country_en', 'country_fr')
    search_fields = ('name_en', 'name_fr',)

class FacultyOptionInline(admin.TabularInline):
    model = FacultyOption
    extra = 1

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_fr', 'icon_name')
    search_fields = ('name_en', 'name_fr',)
    inlines = [FacultyOptionInline]

@admin.register(ProfessionalCourse)
class ProfessionalCourseAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_fr', 'icon_name')
    search_fields = ('name_en', 'name_fr',)
