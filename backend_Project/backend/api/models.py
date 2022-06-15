from django.db import models

class Info(models.Model):
    id = models.CharField(primary_key=True, max_length=12)
    utcdate = models.DateTimeField()
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'info'
        unique_together = (('id', 'utcdate'),)