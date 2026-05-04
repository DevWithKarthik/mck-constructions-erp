from django.db import models

# Daily Attendance
class DailyTask(models.Model):
    employee_name = models.CharField(max_length=100)
    present = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.employee_name


# Weekly Expenses (Driver + Housekeeping)
class WeeklyExpense(models.Model):
    title = models.CharField(max_length=100)  # e.g., Petrol / Food / Housekeeping
    person_name = models.CharField(max_length=100)
    amount = models.FloatField()
    description = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)


# Monthly Salary
class MonthlySalary(models.Model):
    employee_name = models.CharField(max_length=100)
    salary = models.FloatField()
    paid = models.BooleanField(default=False)
    month = models.CharField(max_length=20)
    
    