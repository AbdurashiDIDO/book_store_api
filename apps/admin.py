from PyPDF2 import PdfReader
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.urls import reverse
from django.utils.html import format_html

from apps.models.authors import Author
from apps.models.books import Book
from apps.models.categories import Category


@admin.register(Book)
class BookAdmin(ModelAdmin):
    fields = ('title', 'content', 'category', 'year')
    list_display = ('title', 'pdf_preview',)

    def pdf_preview(self, obj):
        if obj.content:
            return format_html(
                f'<a href="{obj.content}" target="_blank">PDF Preview</a>',

            )
        else:
            return "No PDF available"

    pdf_preview.short_description = 'PDF Preview'

    def save_model(self, request, obj, form, change):
        pdf = request.FILES['content']
        render = PdfReader(pdf)

        category_id = obj.category_id

        book = Book(
            title=form.cleaned_data['title'],
            content=pdf,
            category_id=category_id,
            year=form.cleaned_data['year']
        )

        book.pages = len(render.pages)

        book.save()


admin.site.register(Category)
admin.site.register(Author)
