from django.db import models

# Create your models here.
class Spots(models.Model):
    spot_Num = models.CharField(max_length=3)
    is_taken = models.BooleanField()

    def __str__(self):
        return 'Parking Space #{0}'.format(self.spot_Num)

    class Meta:
        verbose_name_plural = 'Spots'
        