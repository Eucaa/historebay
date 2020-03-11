from django.db import models

# Create your models here.

#To set charfield to lowercase?
"""
def save(self, *args, **kwargs):
    self.yourfiled = self.yourfield.lower()
    return super(ModelsName, self).save(*args, **kwargs)
"""