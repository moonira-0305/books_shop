from django.db import models
from django.utils import timezone
# Create your models here.
class Published_Manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Books.Status.Published)

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
class Author(models.Model):
    full_name= models.CharField(max_length=170)

    def __str__(self):
        return self.full_name
class Books(models.Model):
    class Status(models.TextChoices):
        Draft="DF","Draft"
        Published="PB" "Published"

    title=models.CharField(max_length=250)
    body=models.TextField()
    price=models.CharField(max_length=12)
    image=models.ImageField(upload_to='static/img')
    category=models.ForeignKey(Category,
                               on_delete=models.CASCADE)
    author=models.ForeignKey(Author,
                             on_delete=models.CASCADE)
    publish_time=models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now=True)
    updated_time=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=11,
                            choices=Status.choices,
                            default=Status.Draft
                            )
    class Meta:
        ordering=["-publish_time"]

    objects=models.Manager
    published=Published_Manager

    def __str__(self):
        return self.title