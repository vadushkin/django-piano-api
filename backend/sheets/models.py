from django.core.validators import FileExtensionValidator
from django.db import models
import pypdfium2 as pdfium

from users.models import User


class Author(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['name']


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']


class Sheet(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(validators=[
        FileExtensionValidator(
            allowed_extensions=['pdf'],
            message="It isn't a pdf file"
        )
    ])
    photo = models.ImageField()
    description = models.TextField(blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.SET_NULL, blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name="post", blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        super(Sheet, self).save(*args, **kwargs)
        pdf = pdfium.PdfDocument(f'{self.file.path}')
        page = pdf.get_page(0)
        pil_image = page.render_topil()
        output = f'{self.file.path[:-4]}.jpg'
        pil_image.save(output)
        page.close()
        Sheet.objects.filter(pk=self.pk).update(photo=f'{self.file.path[:-4]}.jpg')

    class Meta:
        verbose_name = 'Sheet'
        verbose_name_plural = 'Sheets'
        ordering = ['name']
