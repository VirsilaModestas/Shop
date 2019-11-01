from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    primary_category = models.BooleanField(default=False)


    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=25)
    mainimage = models.ImageField(upload_to='products/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField()
    previews_text = models.TextField(max_length=120, verbose_name='Preview text')
    detail_text = models.TextField(max_length=250, verbose_name='Detail text')
    price = models.FloatField()


    def __str__(self):
        return self.title
    











