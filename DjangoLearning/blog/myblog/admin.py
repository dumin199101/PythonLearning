from django.contrib import admin
# from .models import *
from . import models
class HeroInfoInline(admin.TabularInline):
    model = models.HeroInfo
    extra = 3

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 2
    fieldsets = [
        ('base',{'fields':['btitle']}),
        ('super',{'fields':['bpub_date']})
    ]
    inlines = [HeroInfoInline]
# Register your models here.
admin.site.register(models.BookInfo,BookInfoAdmin)
admin.site.register(models.HeroInfo)

