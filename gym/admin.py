from django.contrib import admin
from .models import Member
from .models import Equipment 
from .models import Plan
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'membership_type', 'join_date')
    search_fields = ('name', 'email', 'phone')
admin.site.register(Equipment)
admin.site.register(Plan)