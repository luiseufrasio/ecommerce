import random
from pathlib import PurePosixPath
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from .utils import unique_slug_generator

def get_file_name_extension(file_path):
	return PurePosixPath(file_path).stem, PurePosixPath(file_path).suffix 

def upload_image_path(instance, file_name):
	random_name = random.randint(1, 9999999999)
	name, ext = get_file_name_extension(file_name)
	return f'products/{random_name}/{random_name}{ext}'

# Create your models here.
class ProductQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)

	def featured(self):
		return self.filter(featured=True, active=True)

class ProductManager(models.Manager):
	def get_queryset(self):
		return ProductQuerySet(self.model, using=self._db)

	def all(self):
		return self.get_queryset().active()

	def featured(self):
		return self.get_queryset().featured()

	def get_by_id(self, id):
		qs = self.get_queryset().filter(id=id)
		if qs.count() == 1:
			return qs.first()
		return None

class Product(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(blank=True, unique=True)
	description = models.TextField()
	price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
	image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
	featured = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	objects = ProductManager()

	def get_absolute_url(self):
		return reverse("products:detail", kwargs={"slug": self.slug})

	def __str__(self):
		return self.title

def product_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)