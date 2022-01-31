""" Language choices for the language dropdown menus in the ProfileForm """

from django.db.models import TextChoices


class Language(TextChoices):
    """ Language choices """

    ENGLISH = 'English'
    SPANISH = 'Spanish'
    FRENCH = 'French'
    GERMAN = 'German'
    PORTUGUESE = 'Portuguese'
