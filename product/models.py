from django.db import models

# Create your models here.


class User(models.Model):
	id = models.AutoField(primary_key=True)
	full_name = models.CharField(max_length=150, verbose_name="Ism Familiya")
	username = models.CharField(max_length=100, verbose_name="username", blank=True, null=True)
	telegram_id = models.BigIntegerField(verbose_name="Telegram ID", unique=True)



	def __str__(self):
		return f"{id} - {self.full_name} - {self.telegram_id}"




class Product(models.Model):
	id = models.AutoField(primary_key=True)
	productname = models.CharField(verbose_name="Mahsulot nomi", max_length=50)
	photo = models.CharField(verbose_name="Rasm file_id", max_length=200, null=True, blank=True)
	price = models.DecimalField(verbose_name="Narx", decimal_places=2, max_digits=20)
	description = models.TextField(verbose_name="Mahsulot haqida", max_length=3000, null=True, blank=True)

	category_code = models.CharField(verbose_name="Kategoriya kodi", max_length=20)
	category_name = models.CharField(verbose_name="Kategoriya nomi", max_length=30)
	subcategory_code = models.CharField(verbose_name="Ost-kategoriya kodi", max_length=20)
	subcategory_name = models.CharField(verbose_name="Ost-kategoriya nomi", max_length=30)

	def __str__(self):
		return f"№{self.id} - {self.productname}"