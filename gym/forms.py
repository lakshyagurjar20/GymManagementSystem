from django import forms
from .models import Member
from .models import Payment
from .models import Trainer
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['member', 'amount', 'payment_date', 'note']
class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'