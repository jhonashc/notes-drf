from django.db import models
from apps.base.models import BaseModel
from apps.user.models import User

class Note(BaseModel):
    title = models.CharField(max_length=120, null=False)
    content = models.CharField(max_length=240, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
        
    class Meta:
        db_table = 'note'
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'