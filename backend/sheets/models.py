from django.core.validators import FileExtensionValidator
from django.db import models

from sheets.tasks import create_task_photo_of_pdf
from users.models import User


class Author(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ["name"]


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ["name"]


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]


class Sheet(models.Model):
    name = models.CharField(max_length=100)
    file_pdf = models.FileField(
        validators=[
            FileExtensionValidator(
                allowed_extensions=["pdf"],
                message="It isn't a pdf file",
            ),
        ],
    )
    photo = models.ImageField(max_length=200)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(
        Category,
        related_name="category",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    tags = models.ManyToManyField(Tag, related_name="post", blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        super(Sheet, self).save(*args, **kwargs)
        create_task_photo_of_pdf.delay(self.pk, self.file_pdf.url, self.file_pdf.path)

    class Meta:
        verbose_name = "Sheet"
        verbose_name_plural = "Sheets"
        ordering = ["name"]
