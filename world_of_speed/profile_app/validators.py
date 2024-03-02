from django.core.exceptions import ValidationError


def validator_username(value):
    for char in value:
        if not char.isalnum() and char != "_":
            raise ValidationError("Username must contain only letters, digits, and underscores!")


def validate_username_length(value):
    if len(value) < 3:
        raise ValidationError("Username must be at least 3 chars long!")


def validate_year_range(value):
    if value < 1999 or value > 2030:
        raise ValidationError("Year must be between 1999 and 2030!")