import random
import os
from django.db import models

def get_filename_ext(filepath):
    base_name  = os.path.basename(filepath)
    name, ext  = os.path.splittext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename   = random.randint(1,3910209312)
    name, ext      = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
            new_filename=new_filename, 
            final_filename=final_filename
            )

class ProductQureySet(models.query.QuerySet):
    """docstring for ClassName"""
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQureySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self): #Product.objects.featured()
        return self.get_queryset().featured()

	# docstring for ClassName
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) #Product.objects.self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None


# Create your models here.
class Product(models.Model):
    title          = models.CharField(max_length=120)
    slug           = models.SlugField(blank=True, null=True)
    description    = models.TextField()
    price          = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image          = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured       = models.BooleanField(default=False)
    active         = models.BooleanField(default=True)

    objects = ProductManager()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title