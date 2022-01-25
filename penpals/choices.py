from django.db.models import TextChoices


class Language(TextChoices):
    ENG = 'English'
    SPA = 'Spanish'
    FRA = 'French'
    DEU = 'German'
    POR = 'Portuguese'
