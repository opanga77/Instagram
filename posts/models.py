from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='posts_gallery')
    name = models.CharField(max_length=100)
    caption = models.CharField(max_length=200)
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, related_name='images')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
       return reverse('profile', args=[str(self.user.id)])      

class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.comment