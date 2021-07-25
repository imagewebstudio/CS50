from django.contrib import admin
from .models import User, Store, Inventory, Transactions, Register, Movement, Cashierlog, Reciept

# Register your models here
admin.site.register(User)
admin.site.register(Store)
admin.site.register(Inventory)
admin.site.register(Transactions)
admin.site.register(Register)
admin.site.register(Movement)
admin.site.register(Reciept)
admin.site.register(Cashierlog)
