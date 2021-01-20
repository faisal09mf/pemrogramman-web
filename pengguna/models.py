from django.db import models
from datetime import datetime


# Create your models here.
class Pengguna(models.Model):
    nama_pengguna = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    no_hp = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='gambar/%Y/%m/%d/', blank=True)
    deskriptsi = models.TextField(blank=True)
    tanggal_bergabung = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nama_pengguna