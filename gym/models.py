from django.db import models

# Create your models here.


from django.utils import timezone




class Member(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    join_date = models.DateField(auto_now_add=True)
    membership_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Payment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateField(default=timezone.now)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.member.name} - ₹{self.amount} on {self.payment_date}"
class Trainer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    hire_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
class Equipment(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    purchase_date = models.DateField()

    def __str__(self):
        return self.name
    
class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.CharField(max_length=50)  # e.g., '1 Month', '3 Months'
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name