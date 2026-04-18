from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=255)
    emails = models.JSONField(default=list)
    phones = models.JSONField(default=list)
    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["-created_at"]

