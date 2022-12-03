from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator

# Create your models here.


class Author(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    Email_address=models.EmailField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    Caption=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Caption}"


class Posts(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,related_name="posts",null=True)
    image=models.ImageField(upload_to="images",null=True)
    date=models.DateField(default=timezone.now())
    slug=models.SlugField(default="",unique=True,blank=True,null=False)
    excerpt=models.CharField(max_length=100)
    content=models.TextField(validators=[MinLengthValidator(10)])
    caption=models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title} {self.date}"

    class Meta:
        verbose_name_plural="Posts Entity"


class Comment(models.Model):
    user_name=models.CharField(max_length=100)
    user_email=models.EmailField()
    text=models.TextField(validators=[MinLengthValidator(10)])
    post=models.ForeignKey(Posts,on_delete=models.CASCADE,related_name="comments",null=True)








