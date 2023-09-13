from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.ManyToManyField('Tag')
    publication_date = models.DateTimeField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Like(models.Model):
    LIKE_CHOICES = (
        ('like', 'Like'),
        ('unlike', 'Unlike'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)
    like_type = models.CharField(max_length=6, choices=LIKE_CHOICES)

    def __str__(self):
        return f"{self.user.username} {self.like_type}d {self.post.title}"




# Create your models here.
