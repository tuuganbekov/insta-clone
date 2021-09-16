from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class Followings(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')

    def __str__(self):
        return f"{self.from_user}-{self.to_user}"
