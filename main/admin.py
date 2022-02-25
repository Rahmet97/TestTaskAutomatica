from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import ShoppingCenter, Visit, Worker


class ShoppingCenterModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'worker')
    search_fields = ('name',)


admin.site.register(ShoppingCenter, ShoppingCenterModelAdmin)


class WorkerModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name',)


admin.site.register(Worker, WorkerModelAdmin)


class VisitModelAdmin(admin.ModelAdmin):
    """
    ModelAdmin class that prevents modifications through the admin.
    The changelist and the detail view work, but a 403 is returned
    if one actually tries to edit an object.
    Source: https://gist.github.com/aaugustin/1388243
    """
    list_display = ('shopping_center', 'latitude', 'longitude')
    search_fields = ('shopping_center__name', 'shopping_center__worker__name')
    actions = None

    # We cannot call super().get_fields(request, obj) because that method calls
    # get_readonly_fields(request, obj), causing infinite recursion. Ditto for
    # super().get_form(request, obj). So we  assume the default ModelForm.
    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request):
        return False

    # Allow viewing objects but not actually changing them.
    def has_change_permission(self, request, obj=None):
        return (request.method in ['GET', 'HEAD'] and
                super().has_change_permission(request, obj))

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Visit, VisitModelAdmin)
admin.site.unregister((User, Group))
