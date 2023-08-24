from django.contrib import admin
from .models import User, Investment_Plan, Deposit_History, Withdrawal_History
# Register your models here.


admin.site.register(User)
admin.site.register(Investment_Plan)
admin.site.register(Deposit_History)
admin.site.register(Withdrawal_History)