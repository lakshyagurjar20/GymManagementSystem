from django.db import models

# Create your models here.


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
