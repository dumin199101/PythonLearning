from django.db import models

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=200)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(null=False)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'book_info'

class HeroInfo(models.Model):
    hname = models.CharField(max_length=100)
    hgender = models.BooleanField(default=True)
    hcontent = models.TextField()
    isDelete = models.BooleanField(default=False)
    hbook = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
