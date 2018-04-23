from django.db import models
from django.urls import path, reverse
from django.contrib.auth.models import User

# from rest_framework.reverse import reverse as api_reverse


class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null= True, blank=True)
    content = models.TextField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    # # Property is required for read only permission check
    @property
    def owner(self):
        return self.user

    def __str__(self):
        return str(self.user.username)

    # Testing actual url (e.g. retrieve which requires key)
    def get_url(self, request=None):
        return reverse("rest:retrieve", args=str(self.pk),) 

        
        