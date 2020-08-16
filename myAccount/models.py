from django.db import models

# Create your models here.
class newUser(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    mobile = models.IntegerField()
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s %s %s"%(self.name, self.email, self.mobile, self.password)