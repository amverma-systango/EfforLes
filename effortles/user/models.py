from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager


class Department(models.Model):
    department_name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.department_name)


class Designation(models.Model):
    designation_name = models.CharField(max_length=128)
    paid_leaves = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.designation_name)


class User(AbstractUser):
    db_table='auth_user'

    TYPE = [
        ("HR","HR"),
        ("Employee","Employee"),
    ]

    user_type = models.CharField(max_length=10, choices=TYPE)
    reporting_manager = models.ForeignKey('self', on_delete=models.SET_NULL, 
                                            null=True, blank=True)
    department_id = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    designation_id = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)



class Profile(models.Model):
    
    GENDER = [
        ("male", "male"),
        ("female", "female"),
        ("other", "other")
    ]
    
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    contact_no = models.IntegerField()
    profile_url = models.TextField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_id)


class Address(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    country = models.CharField(max_length=128, default=None)
    state = models.CharField(max_length=128, default=None)
    district = models.CharField(max_length=128, default=None)
    city = models.CharField(max_length=128, default=None)
    streat = models.CharField(max_length=128, default=None)
    colony = models.CharField(max_length=128, default=None)
    house_no = models.CharField(max_length=128, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.profile_id)


class UserSalaryRecord(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    base_salary = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_id)


class AppliedLeave(models.Model):

    TYPE_OF_LEAVE = [
        ("Leave","Leave"),
        ("Loss Of Pay","LossOfPay"),
        ("Half Day Leave","Half Day Leave"),
    ]

    STATUS = [
        ("pending", "pending"),
        ("accepted", "accepted"),
        ("rejected", "rejected"),
    ]

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_applied = models.DateField()
    number_of_days = models.IntegerField()
    type_of_leave = models.CharField(max_length=15, choices=TYPE_OF_LEAVE)
    status = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_id)


class Leave(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    paid_leave_balance = models.IntegerField()
    unpaid_leaves_taken = models.IntegerField()
    half_day_leaves_taken = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_id)