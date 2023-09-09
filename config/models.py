from uuid import uuid4

from django.db import models


class BaseModel(models.Model):

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False, unique=True)

    class Meta:
        abstract = True


class BaseTimestampedModel(models.Model):

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Register created timestamp",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Last update timestampt",
    )
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Soft deleted timestamp",
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Indicate if the register is active",
    )

    class Meta:
        abstract = True
