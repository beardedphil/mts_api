from django.db import models


class Source(models.Model):
    source = models.CharField(max_length=25)
    proper_source = models.CharField(max_length=25)

    def __str__(self):
        return self.proper_source
