from django.utils import timezone
from django.db import models
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Phone.Status.Published)
class Category(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='phone/images')

    def __str__(self):
        return self.name


class Phone(models.Model):
    class Status(models.TextChoices):
        Draft = 'DF', 'Draft'
        Published = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, null=True,blank=True,)
    body = models.TextField()
    image1 = models.ImageField(upload_to='phone/images')
    image2 = models.ImageField(upload_to='phone/images')
    image3 = models.ImageField(upload_to='phone/images')
    phonenumber = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)

    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.Draft
                              )
    objects = models.Manager()
    published = PublishedManager()


    class Meta:
        ordering = ['-publish_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_page', args={'slug': self.id})




class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.email