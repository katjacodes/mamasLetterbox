from django.db.models import TextChoices


class Language(TextChoices):
    ENGLISH = 'English'
    SPANISH = 'Spanish'
    FRENCH = 'French'
    GERMAN = 'German'
    PORTUGUESE = 'Portuguese'
