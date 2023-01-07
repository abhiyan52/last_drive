from django.db import models
from last_drive.models import BaseModel
from django.contrib.auth import get_user_model
from last_drive.middleware import get_current_user

User = get_user_model()


class CustomManager(models.Manager):
    # First level of protection in database level
    def get_queryset(self):
        current_user = get_current_user()
        return super().get_queryset().filter(created_by=current_user)


class Artifact(BaseModel):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        db_index=True
    )
    uploaded_file = models.FileField(upload_to="")
    objects = CustomManager()
    excluded_manager = models.Manager()

    def __str__(self):
        return f"{self.name}|{self.created_at}"
