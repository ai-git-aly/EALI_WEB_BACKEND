from django.db import models

class NewsEvent(models.Model):
    CATEGORY_CHOICES = [
        ('Conference', 'Conference'),
        ('Partnership', 'Partnership'),
        ('Admissions', 'Admissions'),
        ('Announcement', 'Announcement'),
        ('Other', 'Other'),
    ]

    title_en = models.CharField(max_length=255)
    title_fr = models.CharField(max_length=255)
    date = models.DateField()
    description_en = models.TextField()
    description_fr = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_en

class NewsImage(models.Model):
    news_event = models.ForeignKey(NewsEvent, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_images/')

    def __str__(self):
        return f"Image for {self.news_event.title_en}"

class Tender(models.Model):
    title_en = models.CharField(max_length=255)
    title_fr = models.CharField(max_length=255)
    description_en = models.TextField()
    description_fr = models.TextField()
    file = models.FileField(upload_to='tenders/')
    date_posted = models.DateField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title_en

class Partner(models.Model):
    TYPE_CHOICES = [
        ('International', 'International'),
        ('National', 'National'),
    ]

    name_en = models.CharField(max_length=255)
    name_fr = models.CharField(max_length=255)
    country_en = models.CharField(max_length=100)
    country_fr = models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    logo = models.ImageField(upload_to='partner_logos/', null=True, blank=True)

    def __str__(self):
        return self.name_en

class Faculty(models.Model):
    name_en = models.CharField(max_length=255) # e.g., faculty_communication
    name_fr = models.CharField(max_length=255)
    icon_name = models.CharField(max_length=50) # e.g., Globe

    def __str__(self):
        return self.name_en

class FacultyOption(models.Model):
    faculty = models.ForeignKey(Faculty, related_name='options', on_delete=models.CASCADE)
    name_en = models.CharField(max_length=255) # e.g., option_communication_development
    name_fr = models.CharField(max_length=255)

    def __str__(self):
        return self.name_en

class ProfessionalCourse(models.Model):
    name_en = models.CharField(max_length=255) # e.g., course_management_accounting
    name_fr = models.CharField(max_length=255)
    icon_name = models.CharField(max_length=50) # e.g., Briefcase

    def __str__(self):
        return self.name_en
