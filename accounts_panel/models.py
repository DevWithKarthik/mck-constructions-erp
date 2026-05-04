from django.db import models

class Expense(models.Model):
    CATEGORY_CHOICES = (
        ('material', 'Material'),
        ('labour', 'Labour'),
        ('transport', 'Transport'),
        ('other', 'Other'),
    )

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    amount = models.FloatField()
    description = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.amount}"


class Income(models.Model):
    source = models.CharField(max_length=100)  # Project name / client
    amount = models.FloatField()
    received_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.source} - {self.amount}"