from django.db import models
from datetime import datetime
from pengguna.models import Pengguna
from phone_field import PhoneField

# Create your models here.
class Jualan(models.Model):
    pengguna = models.ForeignKey(Pengguna, on_delete=models.DO_NOTHING)
    nama_item = models.CharField(max_length=200)
    alamat = models.CharField(max_length=200)
    no_hp = models.CharField(max_length=200)
    deskripsi = models.TextField(blank=True)
    #nama = models.CharField(max_length=200)
    jumlah_kartu = models.IntegerField()
    harga = models.IntegerField()
    is_published = models.BooleanField(default=True)
    tanggal = models.DateTimeField(default=datetime.now, blank=True)
    gambar = models.ImageField(upload_to='gambar/%Y/%m/%d/')
    gambar_1 = models.ImageField(upload_to='gambar/%Y/%m/%d/', blank=True)
    gambar_2 = models.ImageField(upload_to='gambar/%Y/%m/%d/', blank=True)
    gambar_3 = models.ImageField(upload_to='gambar/%Y/%m/%d/', blank=True)
    gambar_4 = models.ImageField(upload_to='gambar/%Y/%m/%d/', blank=True)
    gambar_5 = models.ImageField(upload_to='gambar/%Y/%m/%d/', blank=True)
    def __str__(self):
        return self.nama_item