from django.db import models
from django.db import connections

# Create your models here.
def products():
    id = models.BigIntegerField()
    name = models.CharField()

    class Meta:
        db_table = "products"
