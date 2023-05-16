from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Trades(models.Model):
    SIDE_CHOICES = (("long", "LONG"), ("short", "SHORT"))
    ticker = models.CharField(null=False, blank=False, max_length=10)
    side = models.CharField(null=False, blank=False, max_length=5, choices=SIDE_CHOICES)

    entry = models.DecimalField(null=True, blank=True, max_digits=15, decimal_places=9)
    stop_loss = models.DecimalField(
        null=True, blank=True, max_digits=15, decimal_places=9
    )
    take_profit = models.DecimalField(
        null=True, blank=True, max_digits=15, decimal_places=9
    )
    trade_exit = models.DecimalField(
        null=True, blank=True, max_digits=15, decimal_places=9
    )
    pnl = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    rr = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    tags = models.CharField(null=True, blank=True, max_length=20)
    image = models.ImageField(null=True, blank=True)

    def __str__(self) -> str:
        return self.ticker

    def save(self, *args, **kwargs):
        # set ticker to uppercase
        self.ticker = self.ticker.upper()

        # calculate pnl and rr for trades
        if (
            self.trade_exit
            and self.entry
            and self.stop_loss
            and self.take_profit
            and self.side
        ):
            cal = calculate(
                entry=self.entry,
                sl=self.stop_loss,
                tp=self.take_profit,
                _exit=self.trade_exit,
                side=self.side,
            )
            self.pnl = round(cal["pnl"], 2)
            self.rr = round(cal["rr"], 2)

        print(self.pnl, self.rr)

        super().save(*args, **kwargs)


def calculate(entry, sl, tp, _exit, side):
    pnl = 0
    rr = 0
    if side == "long":
        pnl = _exit - entry
        rr = (tp - entry) / (entry - sl)

    if side == "short":
        pnl = entry - _exit
        rr = (entry - tp) / (sl - entry)

    return {"pnl": pnl, "rr": rr}
