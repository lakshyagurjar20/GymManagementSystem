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
def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_payments')
    else:
        form = PaymentForm()
    return render(request, 'gym/add_payment.html', {'form': form})

def all_payments(request):
    payments = Payment.objects.all().order_by('-payment_date')
    return render(request, 'gym/all_payments.html', {'payments': payments})

@login_required
def dashboard_view(request):
    return render(request, 'gym/dashboard.html')

def login_view(request):
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
    return redirect('login')

def add_member_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        membership_type = request.POST.get('membership_type')

        # Save to database
        Member.objects.create(
            name=name,
            age=age,
            gender=gender,
            phone=phone,
            email=email,
            address=address,
            membership_type=membership_type
        )

        messages.success(request, 'Member added successfully!')
        return redirect('add_member')

    return render(request, 'gym/add_member.html')
def view_members(request):
    members = Member.objects.all()
    return render(request, 'gym/view_members.html', {'members': members})

def all_members_view(request):
    members = Member.objects.all()
    return render(request, 'gym/all_members.html', {'members': members})
def member_detail_view(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    return render(request, 'gym/member_detail.html', {'member': member})


def edit_member_view(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == 'POST':
        member.name = request.POST.get('name')
        member.age = request.POST.get('age')
        member.gender = request.POST.get('gender')
        member.phone = request.POST.get('phone')
        member.email = request.POST.get('email')
        member.address = request.POST.get('address')
        member.membership_type = request.POST.get('membership_type')
        member.save()

        messages.success(request, 'Member updated successfully!')
        return redirect('all_members')

    return render(request, 'gym/edit_member.html', {'member': member})


def delete_member_view(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    if request.method == 'POST':
        member.delete()
        messages.success(request, 'Member deleted successfully!')
        return redirect('all_members')
    return render(request, 'gym/delete_member.html', {'member': member})
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
def delete_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    if request.method == 'POST':
        payment.delete()
        return redirect('all_payments')
    return render(request, 'gym/delete_payment.html', {'payment': payment})
def all_trainers(request):
    trainers = Trainer.objects.all()
    return render(request, 'gym/all_trainers.html', {'trainers': trainers})

def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_trainers')
    else:
        form = TrainerForm()
    return render(request, 'gym/add_trainer.html', {'form': form})

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

def delete_trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, id=trainer_id)
    if request.method == 'POST':
        trainer.delete()
        return redirect('all_trainers')
    return render(request, 'gym/delete_trainer.html', {'trainer': trainer})