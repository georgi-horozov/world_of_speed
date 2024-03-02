from django.core.validators import MinValueValidator
from django.db import models

from world_of_speed.profile_app.validators import validator_username, validate_username_length


class Profile(models.Model):
    MAX_USERNAME_LENGTH = 15
    MIN_AGE_VALUE = 21

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=(validator_username, validate_username_length,),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        help_text="Age requirement: 21 years and above.",
        null=False, blank=False,
        validators=(MinValueValidator(MIN_AGE_VALUE),),
    )

    password = models.CharField(
        max_length=20,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=25,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=25,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
