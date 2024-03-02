from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from world_of_speed.profile_app.models import Profile
from world_of_speed.profile_app.validators import validate_year_range


class Car(models.Model):
    MIN_MODEL_LENGTH = 1
    MAX_MODEL_LENGTH = 15
    MIN_PRICE = 1.0

    TYPE_CHOICES = [
        ('Rally', 'Rally'),
        ('Open-wheel', 'Open-wheel'),
        ('Kart', 'Kart'),
        ('Drag', 'Drag'),
        ('Other', 'Other'),
    ]

    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        blank=False,
        null=False,
        # verbose_name='Type'
    )

    model = models.CharField(
        max_length=MAX_MODEL_LENGTH,
        validators=(MinLengthValidator(MIN_MODEL_LENGTH),),
        null=False,
        blank=False,
    )

    year = models.IntegerField(
        validators=[validate_year_range],
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        unique=True,
        default="https://...",
        verbose_name="Image URL",
        error_messages={
            'unique': "This image URL is already in use! Provide a new one."
        }
    )

    price = models.FloatField(
        validators=(MinValueValidator(MIN_PRICE),),
        null=False,
        blank=False,
    )

    # TODO: The ON DELETE constraint must be configured to an appropriate value in alignment with the specified additional tasks.
    # This field should remain hidden in forms.

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)




