from django.contrib import admin
from .models import Pengguna

# Register your models here.
class PenggunaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_pengguna', 'email', 'tanggal_bergabung')
    list_display_links =  ('id', 'nama_pengguna')


admin.site.register(Pengguna, PenggunaAdmin)