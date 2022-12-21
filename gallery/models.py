from django.db import models
# from django.contrib.auth.models import User
from common.models import User

# Create your models here.
# class TimeStampedModel(models.Model):
#     create_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now_add=True)
#     modify_at = models.DateTimeField(null=True, blank=True)

#     class Meta:
#         abstract = True


class Artwork(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='artwork_author')
    image = models.ImageField()
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    like_users = models.ManyToManyField(User, blank=True, related_name='like_users')
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.subject

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    artwork = models.ForeignKey(Artwork, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.content