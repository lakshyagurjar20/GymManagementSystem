from django import forms
from .models import Member
from .models import Payment
from .models import Trainer
from .models import Equipment
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



class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'
        widgets = {
            'purchase_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
