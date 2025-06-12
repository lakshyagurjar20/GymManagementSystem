from django.urls import path
from .views import signup_view, login_view, logout_view, dashboard_view , add_member_view
from .views import add_member_view, view_members ,all_members_view


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'), 
     path('add-member/', add_member_view, name='add_member'),
     path('members/', view_members, name='view_members'),
      path('add-member/', add_member_view, name='add_member'),
    path('all-members/', all_members_view, name='all_members'),

]
