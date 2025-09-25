from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Banner(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    img = models.ImageField(upload_to='banners/')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

class Gallery(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='galleries/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

class News(models.Model):
    title = models.CharField(max_length=255)
    description = RichTextField()
    img = models.ImageField(upload_to='news/')
    author = models.CharField(max_length=255)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class category(models.Model):
    name = models.CharField(max_length=255)
    about = RichTextField()
    img = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
class categoryItem(models.Model):
    category = models.ForeignKey(category, on_delete=models.CASCADE , related_name='category_items')
    name = models.CharField(max_length=255)
    about = RichTextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category Item'
        verbose_name_plural = 'Category Items'


class ItemImage(models.Model):
    categoryItem = models.ForeignKey(categoryItem, on_delete=models.CASCADE , related_name='item_images')
    img = models.ImageField(upload_to='item_images/')

    def __str__(self):
        return self.categoryItem.name

    class Meta:
        verbose_name = 'Item Image'
        verbose_name_plural = 'Item Images'



class LastItem(models.Model):
    categoryItem = models.ForeignKey(categoryItem, on_delete=models.CASCADE , related_name='last_items')
    name = models.CharField(max_length=255)
    about = RichTextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Last Item'
        verbose_name_plural = 'Last Items'


class LastItemImage(models.Model):
    lastItem = models.ForeignKey(LastItem, on_delete=models.CASCADE , related_name='last_item_images')
    img = models.ImageField(upload_to='last_item_images/')

    def __str__(self):
        return self.lastItem.name

    class Meta:
        verbose_name = 'Last Item Image'
        verbose_name_plural = 'Last Item Images'