from django.db import models


# Create your models here.
class Issue(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        db_table = "issue"
        ordering = ["id"]
