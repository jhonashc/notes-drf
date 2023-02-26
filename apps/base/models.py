from django.db import models

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        verbose_name = 'base_model'
        verbose_name_plural = 'base_models'