from django.db import models
from parsers.models import Parser


class ProductImage(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField()

    def __str__(self):
        return self.url


class Product(models.Model):
    DISCOUNT_TYPES = (
        ('fix', 'Fix'),
        ('percentage', "Percentage")
    )
    parser_id = models.ForeignKey(Parser, on_delete=models.DO_NOTHING)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    url = models.URLField(unique=True)
    images = models.ManyToManyField(ProductImage)
    brand = models.CharField(max_length=100)
    categories = models.CharField(max_length=100)
    discount = models.IntegerField()
    discount_type = models.CharField(choices=DISCOUNT_TYPES, max_length=100)
    sku = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    in_stock = models.IntegerField()
    color = models.CharField(max_length=100, blank=True, null=True)
    made_in = models.CharField(max_length=100, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    depth = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
