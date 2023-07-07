from django.core.validators import FileExtensionValidator
from django.db.models import Model, CharField, PositiveIntegerField, DateField, FileField, ForeignKey, \
    CASCADE


class Book(Model):
    title = CharField(max_length=255)
    content = FileField(upload_to='pdf/', null=True,
                        blank=True,
                        validators=[FileExtensionValidator(['pdf'])])
    pages = PositiveIntegerField(null=True)
    category = ForeignKey('apps.Category', on_delete=CASCADE)
    year = DateField(null=True, blank=True)

    def __str__(self):

        return self.title and self.year.strftime('%d-%m-%Y')

