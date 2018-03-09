from django.db import models
from datetime import datetime

class BookInfoManager(models.Manager):
   def get_queryset(self):
       return super().get_queryset().filter(isDelete=False)

   def create(self,btitle,bpub_date):
       b = BookInfo()
       b.btitle = btitle
       b.bpub_date = bpub_date
       b.bread = 0
       b.bcomment = 0
       b.isDelete = 1
       return b

# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=200)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(null=False)
    isDelete = models.BooleanField(default=False)
    class Meta:
        db_table = 'book_info'
    books1 = models.Manager()
    books2 = BookInfoManager()

    @classmethod
    def create(cls,btitle,bpub_date):
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcomment = 0
        b.isDelete = 1
        return b

    def __str__(self):
        return self.btitle



class HeroInfo(models.Model):
    hname = models.CharField(max_length=100)
    hgender = models.BooleanField(default=True)
    hcontent = models.TextField()
    isDelete = models.BooleanField(default=False)
    hbook = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.hname

    def showName(self):
        return self.hname
