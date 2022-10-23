from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def serialize(self):
        return {
            'title': self.title,
            'body': self.body,
            'image': self.image.url,
        }


class Pin(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='pins', null=True)

    def __str__(self):
        return f'{self.latitude},{self.longitude}'

    def serialize(self):
        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "post": self.post.serialize()
        }
