from django.contrib import admin

from habit_tracker.models import Habit


@admin.register(Habit)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'action')
    search_fields = ('owner', 'action')
    ordering = ("id",)
