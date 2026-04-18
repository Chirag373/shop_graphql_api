from django.db import models

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=255)
    emails = models.JSONField(default=list, blank=True)
    phones = models.JSONField(default=list, blank=True)
    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        # Ensure emails and phones are never None
        if self.emails is None:
            self.emails = []
        if self.phones is None:
            self.phones = []
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ["-created_at"]

