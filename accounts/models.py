from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    image = models.ImageField(upload_to='users/',blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    phonenumber = models.CharField(max_length=18, null=True,blank=True,)

    def __str__(self):
        return f"{self.user.username} profili"

