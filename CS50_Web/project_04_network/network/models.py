from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=48)
    bio = models.TextField(blank=True, max_length=140)
    emoji = models.CharField(max_length=2, blank=True)

    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')
    #symmetrical=False means that if user A follows user B,
    # it doesn't necessarily mean that user B follows user A

    def __str__(self):
        return f"{ self.username }"

    def follow(self, user):
        """
        Follow another user.
        """
        self.following.add(user)

    def unfollow(self, user):
        """
        Unfollow another user.
        """
        self.following.remove(user)

    def is_following(self, user):
        """
        Check if this user is following another user.
        """
        return self.following.filter(pk=user.pk).exists()

    def is_followed_by(self, user):
        """
        Check if this user is followed by another user.
        """
        return user.is_following(self)



class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_notes")
    note_content = models.TextField(blank=True, max_length=280)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.TextField(blank=True)
    likers = models.ManyToManyField(User, blank=True, related_name="liked_by")

    def __str__(self):
        return f"Note by { self.owner } on { self.created }"

class Comments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    note_id = models.ForeignKey(Note, on_delete=models.CASCADE, related_name="all_comments")
    commentator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    comment = models.TextField(blank=True, max_length=280)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by { self.commentator } on { self.date }"

