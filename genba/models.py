from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class CustomAdminUser(BaseUserManager):

    def create_user(self, username, fullname, phone_number, password, note):
        user = self.model(
            username=username,
            fullname=fullname,
            phone_number=phone_number,
            note=note
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_syain_user(self, username, fullname, phone_number, password, note):
        user = self.create_user(
            username=username,
            fullname=fullname,
            phone_number=phone_number,
            note=note
        )
        user.is_staff = True
        user.set_password(password)
        user.save()
        return user
    
    def create_super_user(self, username, fullname, phone_number, password, note):
        user = self.create_user(
            username=username,
            fullname=fullname,
            phone_number=phone_number,
            note=note
        )
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    fullname = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=20)
    note = models.CharField(max_length=500)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ["fullname", "phone_number"]

    def __str__(self):
        return f"{self.username} - {self.fullname} - {self.phone_number}"
    
    class Meta:
        verbose_name_plural = "users"

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


