from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=30, unique=True)
    description = models.TextField()

    class Meta:
        ordering = ["title"]


class Post(models.Model):
    AGE = (
        (0, "5+"),
        (1, "8+"),
        (2, "10+"),
        (3, "13+"),
        (4, "15+"),
        (5, "18+"),
    )

    SKILL = (
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
    )

    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    materials = models.TextField()
    time_taken = models.IntegerField(help_text="Time taken in minutes")
    age = models.IntegerField(choices=AGE, default=0)
    media_url = models.URLField(max_length=200, blank=True, null=True)
    skill = models.IntegerField(choices=SKILL, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="craft_posts"
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    commenter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.content} by {self.commenter}"
