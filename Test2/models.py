from django.db import models
from django.contrib.auth import get_user_model
from Test1.models import Post

User = get_user_model()


class Comment(models.Model):
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment {self.user.username} -> {self.post.title} [{self.created_at}]"
