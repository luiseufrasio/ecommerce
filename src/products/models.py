import random
from pathlib import PurePosixPath
from django.db import models

def get_file_name_extension(file_path):
	return PurePosixPath(file_path).stem, PurePosixPath(file_path).suffix 

def upload_image_path(instance, file_name):
	random_name = random.randint(1, 9999999999)
	name, ext = get_file_name_extension(file_name)
	return f'products/{random_name}/{random_name}{ext}'

# Create your models here.
class ProductManager(models.Manager):
	def get_by_id(self, id):
		qs = self.get_queryset().filter(id=id)
		if qs.count() == 1:
			return qs.first()
		return None

class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()
	price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
	image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

	objects = ProductManager()

	def __str__(self):
		return self.title