# from django.contrib import admin
# from .models import Member
# from .models import Equipment 
# from .models import Plan
# @admin.register(Member)
# class MemberAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'phone', 'membership_type', 'join_date')
#     search_fields = ('name', 'email', 'phone')
# admin.site.register(Equipment)
# admin.site.register(Plan)
from django.contrib import admin
from .models import Member, Equipment, Plan

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone',  'join_date')
    search_fields = ('name', 'email', 'phone')

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity')  # removed 'category'
    search_fields = ('name',)

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'duration')
    search_fields = ('title',)
