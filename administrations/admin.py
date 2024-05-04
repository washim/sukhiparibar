from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer, Emi, Group


class CustomerInline(admin.TabularInline):
    readonly_fields = fields = ['bookno', 'name', 'mobile', 'product_no', 'product_price', 'total_emi_no', 'emi_amount', 'advance_paid', 'emi_paid', 'emi_pending']
    model = Customer
    can_delete = False
    extra = 0


class EmiInline(admin.TabularInline):
    readonly_fields = fields = ['amount', 'due_dt']
    model = Emi
    can_delete = False
    extra = 0


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'bookno', 'name', 'mobile', 'product_no', 'product_name', 'product_price', 'total_emi_no', 'emi_amount', 'advance_paid', 'emi_paid', 'emi_pending', 'advance_paid_date', 'group_id', 'gurdian', 'address')
    search_fields = ['bookno']
    inlines = (EmiInline,)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'leader_name', 'mobile', 'day')
    search_fields = ['name']
    inlines = (CustomerInline,)


@admin.register(Emi)
class EmiAdmin(admin.ModelAdmin):
    list_display = ('cid', 'amount', 'due_dt')