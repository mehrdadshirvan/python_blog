from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

class Country(models.Model):
    id = models.BigAutoField
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = 'Countries'
    def __str__(self):
        return f"{self.name}"


class Address(models.Model):
    id = models.BigAutoField
    full_address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.full_address}"

    class Meta:
        verbose_name_plural = 'Address Entries'

class Customer(models.Model):
    id = models.BigAutoField
    name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    avatar = models.FileField(upload_to="images",default="",null=False)

    def __str__(self):
        return f"{self.name}"

# Create your models here.
class Product(models.Model):
    id = models.BigAutoField
    name = models.CharField(max_length=150)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, related_name="customer")
    slug = models.SlugField(default="",null=False, blank=True,editable=False, db_index=True)
    published_countries = models.ManyToManyField(Country,)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('blog-single-post', args=[self.slug])

    def __str__(self):
        return f"{self.name} ({self.id})"





