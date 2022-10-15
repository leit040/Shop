
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from mixins.models_mixins import PKMixin, UserModel


class Feedback(PKMixin, UserModel):
    text = models.TextField()
    rate = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ],
        default=0
    )
