from django.contrib import admin
from .models import Payme

# Register your models here.
class PaymeAdmin(admin.ModelAdmin):
    list_display = ("id", "phone", "amount", "state", 'status')
    list_display_links = ('id',)
    list_filter = ('status',)
    search_fields = ('status', 'phone', 'amount')


admin.site.register(Payme, PaymeAdmin)
