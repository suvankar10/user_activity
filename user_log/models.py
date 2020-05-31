from django.db import models

# Create your models here.

class users(models.Model):
    real_name=models.CharField(max_length=20)
    user_id=models.CharField(max_length=20)
    tz=models.CharField(max_length=20)
    def __str__(self):
        return self.user_id

class active_period(models.Model):
    user_id=models.CharField(max_length=20)
    start_time=models.CharField(max_length=100)
    end_time=models.CharField(max_length=100)

    def __str__(self):
        return self.user_id
