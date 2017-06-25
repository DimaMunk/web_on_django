from django.db import models

class Subscribers(models.Model):
    email = models.EmailField() # email
    name = models.CharField(max_length=128) # name

    def __str__(self):
        try:
            return "User: {} E-mail: {}".format(self.name, self.email)
        except:
            return '%s' % self.id


    class Meta:
        verbose_name = 'One subscriber'
        verbose_name_plural = 'A lot of subscribers'