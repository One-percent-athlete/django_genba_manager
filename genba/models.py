from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# class CustomUserManager(BaseUserManager):

#     def create_user(self, username, fullname, phone_number, password, note):
#         user = self.model(
#             username=username,
#             fullname=fullname,
#             phone_number=phone_number,
#             password=password,
#             note=note
#         )
#         user.set_password(password)
#         user.save()
#         return user
    
#     def create_syain_user(self, username, fullname, phone_number, password, note):
#         user = self.create_user(
#             username=username,
#             fullname=fullname,
#             phone_number=phone_number,
#             note=note
#         )
#         user.is_staff = True
#         user.set_password(password)
#         user.save()
#         return user
    
#     def create_superuser(self, username, fullname, phone_number, password, note):
#         user = self.create_user(
#             username=username,
#             fullname=fullname,
#             phone_number=phone_number,
#             note=note
#         )
#         user.is_staff = True
#         user.is_superuser = True
#         user.set_password(password)
#         user.save()
#         return user


# class CustomUser(AbstractBaseUser):
#     username = models.CharField(max_length=50, unique=True)
#     fullname = models.CharField(max_length=20, unique=True)
#     phone_number = models.CharField(max_length=20)
#     note = models.CharField(max_length=500)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     objects = CustomUserManager()

#     USERNAME_FIELD = "username"
#     REQUIRED_FIELDS = ["fullname", "phone_number", "note"]

#     def __str__(self):
#         return f"{self.username} - {self.fullname} - {self.phone_number}"
    
#     class Meta:
#         verbose_name_plural = "users"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=30, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    zipcode = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=200, blank=True)
    old_cart = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)

# class Genba(models.Model):
#     name = models.CharField("Genba", max_length=255)
#     client = models.CharField("Client", max_length=255)
#     address = models.CharField("Address", max_length=255)
#     job_description = models.CharField("Job description", max_length=255)
#     remarks = models.CharField("Remarks", max_length=255)
#     start_date = models.DateTimeField("Start date")
#     end_date = models.DateTimeField("End date")
#     person_in_charge = models.ForeignKey( on_delete=)
#     date_created = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.name} - {self.client}"


