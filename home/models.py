from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.



class Categories(models.Model):
    title = models.CharField(max_length=20 , blank = True)

class Product(models.Model):
    category = models.ForeignKey(Categories , on_delete= models.CASCADE)
    name = models.CharField(max_length=12 , unique= True)
    price = models.IntegerField()
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True , blank=True)
    stock = models.IntegerField(default=0)

    def save(self , *args , **kwargs):
        base_slug = slugify(self.name)
        slug = base_slug

        i = 1

        while type(self).objects.filter(slug=slug).exclude(pk=self.pk).exsists():
            # type(self) , return a class that self object point to them
            slug = f"{base_slug}-{i}"

        self.slug=slug

        super().save(*args , **kwargs)
