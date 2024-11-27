from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, Genba, Notification

# Register your models here.
admin.site.register(Profile)
admin.site.register(Genba)
admin.site.register(Notification)

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username']
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)