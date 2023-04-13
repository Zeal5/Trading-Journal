from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class Trade(models.Model):
    DIRECTION_CHOICES = [
        ('long', 'Long'),
        ('short', 'Short'),
    ]

    direction = models.CharField(max_length=5, choices=DIRECTION_CHOICES)

    entry = models.FloatField(blank=False)
    take_profit = models.FloatField(blank=True,null=True)
    stop_loss = models.FloatField(blank=True,null=True)

    notes = models.TextField(max_length=3000,null=True,blank=True)
    image = models.ImageField(upload_to='trades/', null=True, blank=True)
    risk_reward = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    entry_time = models.DateTimeField(null=True, blank=True)
    exit_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Trade {self.pk}"
    
    def clean(self):
        if self.direction == 'long':
            if self.take_profit:
                if self.take_profit < self.entry:
                    raise ValidationError('Take profit cannot be lower than entry')
                
            if self.stop_loss:
                if self.stop_loss > self.entry:
                    raise ValidationError('Stop loss cannot be greater than entry')
        elif self.direction == 'short':
            if self.take_profit:
                if self.take_profit > self.entry:
                    raise ValidationError('Take profit cannot be greater than entry')
            if self.stop_loss:
                if self.stop_loss < self.entry:
                    raise ValidationError('Stop loss cannot be lower than entry')


    def save(self, *args, **kwargs):
        # Calculate risk/reward ratio before saving
        self.full_clean()

        if self.take_profit and self.stop_loss:
            if self.direction == 'long':
                self.risk_reward = (self.take_profit - self.entry) / (self.entry - self.stop_loss)

                
            elif self.direction == 'short':
                self.risk_reward = abs(self.entry - self.take_profit) / (self.stop_loss - self.entry)



        super().save(*args, **kwargs)

