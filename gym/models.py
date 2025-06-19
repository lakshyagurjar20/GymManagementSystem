from django.db import models

# Create your models here.


from django.utils import timezone
 





class Trainer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    hire_date = models.DateField(auto_now_add=True)
    experience = models.PositiveIntegerField(default=0, help_text="Experience in years")

    specialty = models.CharField(max_length=100, default='General')
    salary = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)


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
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.PositiveIntegerField(help_text="Duration in months")

    def __str__(self):
        return self.title


    
class Member(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    join_date = models.DateField(auto_now_add=True)
    

    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.name
    
class Payment(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateField(default=timezone.now)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.member.name} - ₹{self.amount} on {self.payment_date}"
    
    