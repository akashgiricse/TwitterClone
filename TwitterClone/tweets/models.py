from django.conf import settings
from django.db import models
# from django.core.exceptions import ValidationError
# Create your models here.
from .validators import validate_content


class Tweet(models.Model):
    content = models.CharField(max_length=140, validators=[validate_content])
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return str(self.content)

    # def clean(self, *args, **kwargs):
    #     content = self.content
    #     if content == "abc":
    #         raise ValidationError("content cannot be abc ")
    #     return super(Tweet, self).clean(*args, **kwargs)
