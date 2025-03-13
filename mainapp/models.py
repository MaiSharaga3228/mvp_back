from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

from unidecode import unidecode

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=31)
    slug = models.SlugField(max_length=31)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(str(self.name)))
        super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField(max_length=31)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='products', null=True)
    description = models.CharField(max_length=127, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(str(self.name)))
        super().save(*args, **kwargs)


class Cart(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='carts', null=True)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f'Cart {self.id} ({self.owner})'
