from django.db.models import Model, CharField, PositiveIntegerField, ManyToManyField


class Author(Model):
    full_name = CharField(max_length=255)
    books = ManyToManyField('apps.Book')

    def __str__(self):
        return self.full_name



