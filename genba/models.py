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
    note = models.CharField("Note", max_length=255, blank=True, null=True)
    start_date = models.DateTimeField("Start date")
    end_date = models.DateTimeField("End date")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.client}"

class Notification(models.Model):
    author = models.ForeignKey(User, related_name="notification", on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.content} - {self.author} - {self.created_at}"

class Daily_report(models.Model):
    PAYMENT_TYPES = (
        ('現金','現金'),
        ('カード', 'カード'),
        ('電子マネー', '電子マネー'),
        )
    genba = models.ForeignKey(Genba, related_name="genba", on_delete=models.CASCADE)
    distance = models.CharField(max_length=10)
    highway_start = models.CharField(max_length=100, blank=True)
    highway_end = models.CharField(max_length=100, blank=True)
    hightway_payment = models.CharField(max_length=50, choices=PAYMENT_TYPES, blank=True)
    parking = models.CharField(max_length=100, blank=True)
    paid_by = models.ForeignKey(Profile, related_name="paid_by", on_delete=models.CASCADE, null=True, blank=True)
    hotel = models.BooleanField(default=False)
    other_payment = models.CharField(max_length=100, blank=True)
    other_payment_amount = models.CharField(max_length=100, blank=True)
    daily_details = models.CharField(max_length=500, blank=True)
    daily_note = models.CharField(max_length=500, blank=True)
    kentaikyo = models.BooleanField(default=False)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.genba}"



