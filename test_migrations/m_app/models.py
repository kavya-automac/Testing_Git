from django.db import models

# Create your models here.

class Role(models.Model):
    objects = models.Manager()
    name=models.CharField(max_length=100,null=False)

    def __str__(self):  # to display the role name in admin page
        return self.name
