from django.db import models

Status = (
    ('Prosessing' , 'Prosessing'),
    ("Success", "Success"),
    ("Failed", 'Failed'),
    ("Canceled", "Canceled")
)

# Create your models here.
class Payme(models.Model):
    phone = models.CharField(max_length = 13)
    amount = models.CharField(max_length = 200)
    merchant_id = models.CharField(max_length = 500)
    order_key = models.CharField(max_length = 200, null = True)
    state = models.IntegerField()
    status = models.CharField(max_length = 200, choices = Status)
    trans_date = models.DateTimeField(auto_now = True)
    cancelde_time = models.DateTimeField(auto_now = True)
    reason = models.IntegerField(null = True)


    def __str__(self) -> str:
        return f'{self.phone} --- {self.status}'
