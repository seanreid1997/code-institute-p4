from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Posted'))


class Post(models.Model):

    """
    Class for posts added to databse(temporary docstring)
    """
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    user_text = models.TextField()
    exerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Class for comments added to database(temporary docstring)
    """
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.text} by {self.name}"
