from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .models import Member
from django.shortcuts import get_object_or_404

from .forms import MemberForm

from .forms import PaymentForm
from .models import Payment
from .models import Trainer
from .forms import TrainerForm
from .models import Equipment
from .forms import EquipmentForm
from .models import Plan
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomUserCreationForm
from .forms import MemberForm
@login_required
def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_payments')
    else:
        form = PaymentForm()
    return render(request, 'gym/add_payment.html', {'form': form})
@login_required
def all_payments(request):
    payments = Payment.objects.all().order_by('-payment_date')
    return render(request, 'gym/all_payments.html', {'payments': payments})

@login_required
def dashboard_view(request):
    return render(request, 'gym/dashboard.html')

def login_view(request):
     if request.user.is_authenticated:
        return redirect('gym/dashboard')
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")

     return render(request, 'gym/login.html')

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('gym/dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password != confirm:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')

    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')
@login_required
def add_member_view(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member added successfully!')
            return redirect('add_member')
    else:
        form = MemberForm()
    return render(request, 'gym/add_member.html', {'form': form})
@login_required
def view_members(request):
    members = Member.objects.all()
    return render(request, 'gym/view_members.html', {'members': members})

from django.contrib.auth.decorators import login_required

@login_required
def all_members_view(request):
    query = request.GET.get('q')
    if query:
        members = Member.objects.filter(name__icontains=query)
    else:
        members = Member.objects.all()
    return render(request, 'gym/all_members.html', {'members': members})

@login_required
def member_detail_view(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    return render(request, 'gym/member_detail.html', {'member': member})

@login_required
@login_required
def edit_member_view(request, member_id):
    member = get_object_or_404(Member, id=member_id)

    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member updated successfully!')
            return redirect('view_member', member_id=member.id)
    else:
        form = MemberForm(instance=member)

    return render(request, 'gym/edit_member.html', {'form': form, 'member': member})

@login_required
def delete_member_view(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == 'POST':
        member.delete()
        messages.success(request, 'Member deleted successfully!')
        return redirect('all_members')
    return render(request, 'gym/delete_member.html', {'member': member})
@login_required
def edit_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('all_payments')
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'gym/add_payment.html', {'form': form, 'edit': True})

# Delete Payment
@login_required
def delete_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    if request.method == 'POST':
        payment.delete()
        return redirect('all_payments')
    return render(request, 'gym/delete_payment.html', {'payment': payment})
@login_required
def all_trainers(request):
    trainers = Trainer.objects.all()
    return render(request, 'gym/all_trainers.html', {'trainers': trainers})
@login_required
def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_trainers')
    else:
        form = TrainerForm()
    return render(request, 'gym/add_trainer.html', {'form': form})
@login_required
def edit_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('all_trainers')
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'gym/edit_trainer.html', {'form': form, 'trainer': trainer})
@login_required
def delete_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    if request.method == 'POST':
        trainer.delete()
        return redirect('all_trainers')
    return render(request, 'gym/delete_trainer.html', {'trainer': trainer})


# List all equipment
@login_required
def all_equipment(request):
    equipments = Equipment.objects.all()
    return render(request, 'gym/all_equipment.html', {'equipments': equipments})

# Add new equipment
@login_required
def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_equipment')
    else:
        form = EquipmentForm()
    return render(request, 'gym/add_equipment.html', {'form': form})

# Edit equipment
@login_required
def edit_equipment(request, eid):
    equipment = Equipment.objects.get(id=eid)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('all_equipment')
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'gym/edit_equipment.html', {'form': form})

# Delete equipment
@login_required
def delete_equipment(request, eid):
    equipment = Equipment.objects.get(id=eid)
    if request.method == 'POST':
        equipment.delete()
        return redirect('all_equipment')
    return render(request, 'gym/delete_equipment.html', {'equipment': equipment})
@login_required
def all_plans(request):
    plans = Plan.objects.all()
    return render(request, 'gym/all_plans.html', {'plans': plans})

# Add new plan
@login_required
def add_plan(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        duration = request.POST.get('duration')
        Plan.objects.create(title=title, price=price, duration=duration)
        return redirect('all_plans')
    return render(request, 'gym/add_plan.html')

# Edit plan
@login_required
def edit_plan(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)
    if request.method == 'POST':
        plan.title = request.POST.get('title')
        plan.price = request.POST.get('price')
        plan.duration = request.POST.get('duration')
        plan.save()
        return redirect('all_plans')
    return render(request, 'gym/edit_plan.html', {'plan': plan})

# Delete plan
@login_required
def delete_plan(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)

    # Detach plan from all members before deletion
    Member.objects.filter(plan=plan).update(plan=None)

    plan.delete()
    return redirect('all_plans')


@login_required
def dashboard_view(request):
    total_members = Member.objects.count()
    total_trainers = Trainer.objects.count()
    total_payments = Payment.objects.count()

    context = {
        'total_members': total_members,
        'total_trainers': total_trainers,
        'total_payments': total_payments,
    }
    return render(request, 'gym/dashboard.html', context)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # We'll define login view soon
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})