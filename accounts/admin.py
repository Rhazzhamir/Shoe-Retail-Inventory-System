# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.models import User ,Group
from .models import AuditTrail
from django.contrib.admin import AdminSite


# Register your models here.
# admin.site.unregister(User)
admin.site.unregister(Group)

class AuditTrailAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'timestamp')
    list_filter = ('action', 'timestamp')
    search_fields = ('user__username',)

admin.site.register(AuditTrail, AuditTrailAdmin)

class MyAdminSite(AdminSite):
    def has_permission(self, request):
        return request.user.is_active and request.user.is_superuser

admin_site = MyAdminSite(name='myadmin')
admin_site.register(AuditTrail, AuditTrailAdmin)
