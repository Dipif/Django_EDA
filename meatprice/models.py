from django.db import models

# Create your models here.


class MeatSetting(models.Model) :
    def __str__(self):
        return self.plot_type
    plot_type = models.CharField(default = "Nothing", max_length = 10, null=True)