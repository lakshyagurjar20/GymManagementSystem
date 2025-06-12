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

]
