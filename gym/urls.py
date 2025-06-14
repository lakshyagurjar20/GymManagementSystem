from django.urls import path
from .views import signup_view, login_view, logout_view, dashboard_view , add_member_view
from .views import  view_members ,all_members_view ,member_detail_view, edit_member_view, delete_member_view

from . import views

urlpatterns = [
    
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'), 
     path('add-member/', add_member_view, name='add_member'),
     path('members/', view_members, name='view_members'),
      path('add-member/', add_member_view, name='add_member'),
    path('all-members/', all_members_view, name='all_members'),
    path('member/<int:member_id>/', member_detail_view, name='member_detail'),
    path('member/<int:member_id>/edit/', edit_member_view, name='edit_member'),
    path('member/<int:member_id>/delete/', delete_member_view, name='delete_member'),
    path('add-payment/', views.add_payment, name='add_payment'),
    path('all-payments/', views.all_payments, name='all_payments'),
    path('edit-payment/<int:payment_id>/', views.edit_payment, name='edit_payment'),
    path('delete-payment/<int:payment_id>/', views.delete_payment, name='delete_payment'),
    path('all-trainers/', views.all_trainers, name='all_trainers'),
    path('add-trainer/', views.add_trainer, name='add_trainer'),
    path('edit-trainer/<int:trainer_id>/', views.edit_trainer, name='edit_trainer'),
    path('delete-trainer/<int:trainer_id>/', views.delete_trainer, name='delete_trainer'),
    path('all-equipment/', views.all_equipment, name='all_equipment'),
    path('add-equipment/', views.add_equipment, name='add_equipment'),
    path('edit-equipment/<int:eid>/', views.edit_equipment, name='edit_equipment'),
    path('delete-equipment/<int:eid>/', views.delete_equipment, name='delete_equipment'),
    # Plan URLs
     path('all-plans/', views.all_plans, name='all_plans'),
    path('add-plan/', views.add_plan, name='add_plan'),
    path('edit-plan/<int:plan_id>/', views.edit_plan, name='edit_plan'),
    path('delete-plan/<int:plan_id>/', views.delete_plan, name='delete_plan'),
    path('dashboard/', views.dashboard_view, name='dashboard'),

]
