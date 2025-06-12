from django import forms
from .models import Member
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['member', 'amount', 'payment_date', 'note']
class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
