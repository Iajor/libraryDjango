from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=200)
    edition = models.PositiveIntegerField()
    publication_year = models.PositiveIntegerField()
    authors = models.ManyToManyField(Author, related_name='books')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
