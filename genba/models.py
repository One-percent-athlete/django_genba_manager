from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    CONTRACT_TYPES = (
        ('元請', '元請'),
        ('正社員', '正社員'),
        ('管理', '管理'),
    )
    contract_type = models.CharField(max_length=50, choices=CONTRACT_TYPES, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    note = models.CharField(max_length=500, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.fullname}"
    

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)

class Genba(models.Model):
    head_person = models.ForeignKey(Profile, related_name="head_person", on_delete=models.CASCADE, null=True)
    attendees = models.ManyToManyField(Profile, related_name="attendees", blank=True)
    name = models.CharField("Genba", max_length=255)
    client = models.CharField("Client", max_length=255)
    address = models.CharField("Address", max_length=255)
    job_description = models.CharField("Job description", max_length=255, blank=True, null=True)
    note = models.CharField("Remarks", max_length=255, blank=True, null=True)
    start_date = models.DateTimeField("Start date")
    end_date = models.DateTimeField("End date")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.client} - {self.head_person}"

class Notification(models.Model):
    author = models.ForeignKey(User, related_name="notification", on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.content} - {self.author} - {self.created_at}"
