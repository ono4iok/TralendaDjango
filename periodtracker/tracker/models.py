from django.db import models
from datetime import timedelta

class Cycle(models.Model):
    last_period_date = models.DateField()
    cycle_length = models.IntegerField(default=28)  # typical cycle
    created_at = models.DateTimeField(auto_now_add=True)

    def next_period(self):
        return self.last_period_date + timedelta(days=self.cycle_length)

    def ovulation_day(self):
        # Ovulation usually occurs 14 days before next period
        return self.next_period() - timedelta(days=14)

    def fertile_window_start(self):
        # Fertile window begins 5 days before ovulation
        return self.ovulation_day() - timedelta(days=5)

    def fertile_window_end(self):
        return self.ovulation_day() + timedelta(days=1)

    def __str__(self):
        return f"Cycle starting {self.last_period_date}"

class PeriodHistory(models.Model):
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Period from {self.start_date} to {self.end_date}"

class SexHistory(models.Model):
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    date = models.DateField()
    protected = models.BooleanField(default=True)

    def __str__(self):
        return f"Sex on {self.date}"
