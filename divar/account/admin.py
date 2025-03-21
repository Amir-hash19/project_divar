from django.contrib import admin
from account.models import Account
from django.utils import timezone

class AccountAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "mobile", "date_joined")
    list_filter = ("username",)
    search_fields = ("username", "email")
    fields = (("username", "email"), "mobile", "date_joined")
    list_per_page = 20


    def get_ordering(self, request):
        if request.user.is_superuser:
            return ("username", "email")
        return ("username", )

admin.site.register(Account)
