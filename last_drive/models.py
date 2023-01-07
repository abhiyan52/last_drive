from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, db_index=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)s_created")
    modified_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="%(class)s_modified")

    class Meta:
        abstract = True
