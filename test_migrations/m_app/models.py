from django.db import models

# Create your models here.

class Role(models.Model):
    objects = models.Manager()
    namee=models.CharField(max_length=100,null=False)

    def __str__(self):  # to display the role name in admin page
        return self.name

class Role1(models.Model):
    objects = models.Manager()
    name1=models.CharField(max_length=100,null=False)

    def __str__(self):  # to display the role name in admin page
        return self.name1

class Role2(models.Model):
    objects = models.Manager()
    name2=models.CharField(max_length=100,null=False)

    def __str__(self):  # to display the role name in admin page
        return self.name2

class test(models.Model):
    objects = models.Manager()
    testing=models.CharField(max_length=100,null=False)

    def __str__(self):  # to display the role name in admin page
        return self.testing