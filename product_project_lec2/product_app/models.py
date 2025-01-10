from django.db import models

# Create your models here.
class Product(models.Model):
    prdno = models.CharField(db_column='prdNo', primary_key=True, max_length=10)  # Field name made lowercase.
    prdname = models.CharField(db_column='prdName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prdprice = models.IntegerField(db_column='prdPrice', blank=True, null=True)  # Field name made lowercase.
    prdmaker = models.CharField(db_column='prdMaker', max_length=30, blank=True, null=True)  # Field name made lowercase.
    prdcolor = models.CharField(db_column='prdColor', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ctgno = models.CharField(db_column='ctgNo', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'