from django.db import models

# Create your models here.

class Bookmark(models.Model):
    site_name = models.CharField('사이트명',max_length=100)
    url = models.URLField('사이트URL')

    class Meta:
        ordering = ['-site_name','url']

    def __str__(self):
        return self.site_name

    def get_absolute_url(self):
        pass