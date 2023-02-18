from djongo import models

class PriceHistory(models.Model):
    asset_name = models.CharField(max_length=100)
    is_available = models.JSONField()
    timestamp = models.DateTimeField()

    class Meta:
        db_table = 'priceHistory'
        app_label = 'staking_status_app'
        managed = True
        # using = 'mongoDb'

PriceHistory._meta.using = "mongoDb"
