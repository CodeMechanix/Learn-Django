from django.db import models
from django.conf import settings

# class Destination:
#     id: int
#     name: str
#     img: str
#     desc: str
#     price: int 
#     offer: bool
User = settings.AUTH_USER_MODEL

class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    offer = models.BooleanField(default=False)

class Testimonial(models.Model):
    message = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    user_type = models.CharField(max_length=50)

class Book(models.Model):
    book_name = models.CharField(max_length=500)
    book_writter = models.CharField(max_length=500)
    book_type = models.CharField(max_length=200)

class url_access(models.Model):
    url_id = models.CharField(max_length=500)

class Roleurl(models.Model):
    user_type = models.CharField(max_length=500)
    valid_url = models.CharField(max_length=500)

def __str__(self):
    return self.name


