from django.db import models

# Create your models here.
class StockDetail(models.Model):
    ticker = models.CharField(max_length = 10)
    opens = models.FloatField()
    closes = models.FloatField()
    volume = models.FloatField()

    def __str__(self):
        return self.ticker
