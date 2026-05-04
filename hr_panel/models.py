from django.db import models

class Candidate(models.Model):
    STAGE_CHOICES = (
        (1, 'First Round'),
        (2, 'Second Technical'),
        (3, 'Client Technical'),
        (4, 'Technical HR'),
        (5, 'Final Decision'),
    )

    name = models.CharField(max_length=100)
    stage = models.IntegerField(choices=STAGE_CHOICES, default=1)

    selected = models.BooleanField(null=True, blank=True)
    remarks = models.TextField(blank=True)

    joining_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name