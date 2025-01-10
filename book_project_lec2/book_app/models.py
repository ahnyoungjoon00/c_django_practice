from django.db import models

# Create your models here.
class Book(models.Model):
    bookno = models.CharField(db_column='bookNo', primary_key=True, max_length=10)  # Field name made lowercase.
    bookname = models.CharField(db_column='bookName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bookauthor = models.CharField(db_column='bookAuthor', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bookprice = models.BigIntegerField(db_column='bookPrice', blank=True, null=True)  # Field name made lowercase.
    bookdate = models.CharField(db_column='bookDate', max_length=30, blank=True, null=True)  # Field name made lowercase.
    bookstock = models.IntegerField(db_column='bookStock', blank=True, null=True)  # Field name made lowercase.
    #pubno = models.CharField(db_column='pubNo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    pubno = models.ForeignKey('Publisher', models.DO_NOTHING, db_column='pubNo', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'book'

class Publisher(models.Model):
    # 클래스 속성(변수)
    pubno = models.CharField(db_column='pubNo', primary_key=True, max_length=10)  # Field name made lowercase.
    pubname = models.CharField(db_column='pubName', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'publisher' 
    # 메소드(함수)
    def __str__(self) :
        return str(self.pubname)