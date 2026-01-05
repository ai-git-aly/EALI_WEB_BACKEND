import os
import django
import sys

# Add the backend directory to the sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_core.settings')
django.setup()

from api.models import NewsEvent, Partner, Faculty, FacultyOption, ProfessionalCourse

def seed_data():
    # 1. News Events
    news_data = [
        {
            'title': 'EALI.BI Annual Leadership Conference 2024',
            'date': '2024-03-15',
            'description': 'Join us for our annual leadership conference featuring keynote speakers from across East Africa.',
            'category': 'Conference'
        },
        {
            'title': 'New Partnership with Kabale University',
            'date': '2024-02-28',
            'description': 'EALI.BI signs MOU with Kabale University Uganda for student exchange programs.',
            'category': 'Partnership'
        },
        {
            'title': 'Admissions Open for 2024 Academic Year',
            'date': '2024-01-15',
            'description': 'Applications are now open for all bachelor and diploma programs.',
            'category': 'Admissions'
        },
        {
            'title': 'The new developer of EALI.bi University',
            'date': '2025-12-30',
            'description': 'The new developer of EALI.bi University is announced.',
            'category': 'Announcement'
        }
    ]

    for item in news_data:
        NewsEvent.objects.get_or_create(
            title_en=item['title'],
            defaults={
                'title_fr': item['title'],
                'date': item['date'],
                'description_en': item['description'],
                'description_fr': item['description'],
                'category': item['category']
            }
        )
    print("Seeded News Events")

    # 2. Partners
    partners_data = {
        'international': [
            { 'name': 'Kabale University', 'country': 'Uganda' },
            { 'name': 'Centre International de Recherche pour le Développement Durable (CIRDD)', 'country': 'International' },
            { 'name': 'Pareto University', 'country': 'United Kingdom' },
            { 'name': 'Université Evangelique en Afrique (UEA)', 'country': 'RDC' },
            { 'name': 'Institut Supérieur de Développement Rural (ISDR)', 'country': 'RDC' }
        ],
        'national': [
            { 'name': 'Université du Burundi', 'country': 'Burundi' },
            { 'name': 'Université de Ngozi', 'country': 'Burundi' },
            { 'name': 'Universités privées au Burundi', 'country': 'Burundi' },
            { 'name': 'Gouvernement du Burundi (Ministère de l’environnement, de l’agriculture et de l’élevage, Ministère de l’éducation nationale et de la recherche scientifique)', 'country': 'Burundi' },
            { 'name': 'Institut des Sciences Agronomiques du Burundi (ISABU)', 'country': 'Burundi' },
            { 'name': 'US Embassy du Burundi', 'country': 'Burundi' },
            { 'name': 'Higher Life Foundation', 'country': 'Burundi' }
        ]
    }

    for partner in partners_data['international']:
        Partner.objects.get_or_create(
            name_en=partner['name'], 
            defaults={
                'name_fr': partner['name'],
                'country_en': partner['country'], 
                'country_fr': partner['country'], 
                'type': 'International'
            }
        )
    
    for partner in partners_data['national']:
        Partner.objects.get_or_create(
            name_en=partner['name'], 
            defaults={
                'name_fr': partner['name'],
                'country_en': partner['country'], 
                'country_fr': partner['country'], 
                'type': 'National'
            }
        )
    print("Seeded Partners")

    # 3. Faculties and Options
    faculties_data = [
        {
            'name': 'faculty_communication',
            'icon_name': 'Globe',
            'options': ['option_communication_development']
        },
        {
            'name': 'faculty_economics_management',
            'icon_name': 'Briefcase',
            'options': ['option_management_accounting', 'option_community_development']
        },
        {
            'name': 'faculty_health',
            'icon_name': 'BookOpen',
            'options': ['option_public_health', 'option_human_nutrition']
        },
        {
            'name': 'faculty_tech',
            'icon_name': 'Cpu',
            'options': ['option_network_management', 'option_it_maintenance', 'option_business_computing']
        },
        {
            'name': 'faculty_agronomy',
            'icon_name': 'Sprout',
            'options': ['option_plant_production', 'option_animal_production', 'option_food_security']
        }
    ]

    for f_data in faculties_data:
        faculty, created = Faculty.objects.get_or_create(
            name_en=f_data['name'], 
            defaults={
                'name_fr': f_data['name'],
                'icon_name': f_data['icon_name']
            }
        )
        for opt_name in f_data['options']:
            FacultyOption.objects.get_or_create(
                faculty=faculty, 
                name_en=opt_name,
                defaults={'name_fr': opt_name}
            )
    print("Seeded Faculties")

    # 4. Professional Courses
    courses_data = [
        {'name': 'course_management_accounting', 'icon_name': 'Briefcase'},
        {'name': 'course_community_development', 'icon_name': 'Globe'},
        {'name': 'course_telecom_networks', 'icon_name': 'Wifi'},
        {'name': 'course_it_maintenance', 'icon_name': 'Cpu'},
        {'name': 'course_hospitality_tourism', 'icon_name': 'Briefcase'},
        {'name': 'course_agriculture_development', 'icon_name': 'Sprout'},
        {'name': 'course_livestock_development', 'icon_name': 'Sprout'}
    ]

    for c_data in courses_data:
        ProfessionalCourse.objects.get_or_create(
            name_en=c_data['name'], 
            defaults={
                'name_fr': c_data['name'],
                'icon_name': c_data['icon_name']
            }
        )
    print("Seeded Professional Courses")

if __name__ == '__main__':
    seed_data()
    print("Database seeding complete!")
