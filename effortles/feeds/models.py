from django.db import models
from django.conf import settings

class Post(models.Model):
    owner_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_message = models.TextField()
    content_url = models.TextField()
    comment_count = models.IntegerField()
    like_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class Comment(models.Model):
    post_id = models.ForeignKey( Post, on_delete = models.CASCADE )
    commenter_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment_message = models.CharField(max_length=512)
    like_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
    

class Like(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


class CommentLike(models.Model):

    # user_id = models.ForeignKey()
    comment_id = models.ForeignKey(Comment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


