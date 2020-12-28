from django.db import models
from django.contrib.postgres.fields import ArrayField


class Article(models.Model):
    title = models.CharField(max_length=200)
    source = models.CharField(max_length=25)
    article_link = models.URLField()
    image_link = models.URLField()
    pub_date = models.DateField()
    keywords = ArrayField(
        models.CharField(max_length=50),
        blank=True
    )

    def __str__(self):
        return self.title
