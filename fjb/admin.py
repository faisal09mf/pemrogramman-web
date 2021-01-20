from django.contrib import admin
from .models import Jualan


# Register your models here.
class JualanAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_item', 'harga', 'pengguna', 'is_published', 'tanggal')
    list_display_links = ('id', 'nama_item')
    list_filter = ('pengguna', 'is_published')
    list_edtable = ('is_published',)

admin.site.register(Jualan, JualanAdmin)
