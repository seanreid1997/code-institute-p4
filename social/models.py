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


class Profile(models.Model):
    """
    temp docstring
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    profile_image = CloudinaryField('image', default='https://t3.ftcdn.net/jpg/03/46/83/96/360_F_346839683_6nAPzbhpSkIpb8pmAwufkC7c5eD7wYws.jpg')

    def __str__(self):
        return self.user.name
