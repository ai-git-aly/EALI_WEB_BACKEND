import os
import sys
import django
from django.core.files import File
from pathlib import Path
import shutil

# Setup Django environment
sys.path.append(str(Path(__file__).resolve().parent.parent))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_core.settings')
django.setup()

from api.models import NewsEvent, NewsImage, Tender, Partner, Faculty, FacultyOption, ProfessionalCourse

def run_seed():
    print("Seeding data...")

    # Clear existing data
    NewsEvent.objects.all().delete()
    Tender.objects.all().delete()
    Partner.objects.all().delete()
    Faculty.objects.all().delete()
    ProfessionalCourse.objects.all().delete()

    # 1. News Events
    print("Creating News Events...")
    
    # Specific News Item
    news_item = NewsEvent.objects.create(
        title="Remise des diplômes à l'East African Leadership Institute",
        date="2022-09-09",
        description="Vendredi le 09 septembre s’est tenu les cérémonies de remise des diplômes à l’East African Leadership Institute. 350 lauréats ont été diplomés.",
        category="Announcement"
    )
    
    # Add images to the specific news item
    # Assuming images are in a known location, we'll copy them
    # You need to ensure these paths are correct based on where the agent put them
    image_paths = [
        r"C:/Users/Ally/.gemini/antigravity/brain/723e3199-8062-4396-9908-30d3125cbedd/uploaded_image_0_1767539857505.jpg",
        r"C:/Users/Ally/.gemini/antigravity/brain/723e3199-8062-4396-9908-30d3125cbedd/uploaded_image_1_1767539857505.jpg",
        r"C:/Users/Ally/.gemini/antigravity/brain/723e3199-8062-4396-9908-30d3125cbedd/uploaded_image_2_1767539857505.jpg"
    ]
    
    for img_path in image_paths:
        if os.path.exists(img_path):
            with open(img_path, 'rb') as f:
                NewsImage.objects.create(news_event=news_item, image=File(f, name=os.path.basename(img_path)))
        else:
            print(f"Warning: Image not found at {img_path}")

    # Other News from index.ts
    NewsEvent.objects.create(
        title='EALI.BI Annual Leadership Conference 2024',
        date='2024-03-15',
        description='Join us for our annual leadership conference featuring keynote speakers from across East Africa.',
        category='Conference'
    )
    NewsEvent.objects.create(
        title='New Partnership with Kabale University',
        date='2024-02-28',
        description='EALI.BI signs MOU with Kabale University Uganda for student exchange programs.',
        category='Partnership'
    )
    NewsEvent.objects.create(
        title='Admissions Open for 2024 Academic Year',
        date='2024-01-15',
        description='Applications are now open for all bachelor and diploma programs.',
        category='Admissions'
    )

    # 2. Partners
    print("Creating Partners...")
    partners_data = [
        {'name': 'Kabale University', 'country': 'Uganda', 'type': 'International'},
        {'name': 'Centre International de Recherche pour le Développement Durable (CIRDD)', 'country': 'International', 'type': 'International'},
        {'name': 'Pareto University', 'country': 'United Kingdom', 'type': 'International'},
        {'name': 'Université Evangelique en Afrique (UEA)', 'country': 'RDC', 'type': 'International'},
        {'name': 'Institut Supérieur de Développement Rural (ISDR)', 'country': 'RDC', 'type': 'International'},
        {'name': 'Université du Burundi', 'country': 'Burundi', 'type': 'National'},
        {'name': 'Université de Ngozi', 'country': 'Burundi', 'type': 'National'},
        {'name': 'Universités privées au Burundi', 'country': 'Burundi', 'type': 'National'},
        {'name': 'Gouvernement du Burundi', 'country': 'Burundi', 'type': 'National'},
        {'name': 'Institut des Sciences Agronomiques du Burundi (ISABU)', 'country': 'Burundi', 'type': 'National'},
        {'name': 'US Embassy du Burundi', 'country': 'Burundi', 'type': 'National'},
        {'name': 'Higher Life Foundation', 'country': 'Burundi', 'type': 'National'},
    ]
    for p in partners_data:
        Partner.objects.create(**p)

    # 3. Faculties
    print("Creating Faculties...")
    faculties_data = [
        {'name': 'faculty_communication', 'icon': 'Globe', 'options': ['option_communication_development']},
        {'name': 'faculty_economics_management', 'icon': 'Briefcase', 'options': ['option_management_accounting', 'option_community_development']},
        {'name': 'faculty_health', 'icon': 'BookOpen', 'options': ['option_public_health', 'option_human_nutrition']},
        {'name': 'faculty_tech', 'icon': 'Cpu', 'options': ['option_network_management', 'option_it_maintenance', 'option_business_computing']},
        {'name': 'faculty_agronomy', 'icon': 'Sprout', 'options': ['option_plant_production', 'option_animal_production', 'option_food_security']},
    ]
    for f_data in faculties_data:
        faculty = Faculty.objects.create(name=f_data['name'], icon_name=f_data['icon'])
        for opt in f_data['options']:
            FacultyOption.objects.create(faculty=faculty, name=opt)

    # 4. Professional Courses
    print("Creating Professional Courses...")
    courses_data = [
        {'name': 'course_management_accounting', 'icon': 'Briefcase'},
        {'name': 'course_community_development', 'icon': 'Globe'},
        {'name': 'course_telecom_networks', 'icon': 'Wifi'},
        {'name': 'course_it_maintenance', 'icon': 'Cpu'},
        {'name': 'course_hospitality_tourism', 'icon': 'Briefcase'},
        {'name': 'course_agriculture_development', 'icon': 'Sprout'},
        {'name': 'course_livestock_development', 'icon': 'Sprout'},
    ]
    for c_data in courses_data:
        ProfessionalCourse.objects.create(name=c_data['name'], icon_name=c_data['icon'])

    # 5. Tenders (Appel d'offre)
    print("Creating Tenders...")
    pdf_path = r"c:/Users/Ally/Desktop/react_app/dist/assets/TERMES-DE-REFERENCES-RELATIFS-AU-RECRUTEMENT-DUN-CONSULTANT-INTERNATIONAL-ETUDE-DE-BASE-12.pdf"
    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as f:
            Tender.objects.create(
                title="TERMES DE REFERENCES RELATIFS AU RECRUTEMENT D'UN CONSULTANT INTERNATIONAL",
                description="Appel d'offre pour le recrutement d'un consultant international.",
                file=File(f, name=os.path.basename(pdf_path))
            )
    else:
        print(f"Warning: PDF not found at {pdf_path}")

    print("Seeding completed successfully.")

if __name__ == '__main__':
    run_seed()
