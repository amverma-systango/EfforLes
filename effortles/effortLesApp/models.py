from email.headerregistry import Address
import profile
from time import time
from tkinter import CASCADE
from turtle import mode, update
from venv import create
from django.db import models
from django.forms import CharField, DateField, IntegerField


class Department(models.Model):
    department_name = models.CharField(max_length=128)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)


class Designation(models.Model):
    designation_name= models.CharField(max_length=128)
    paid_leaves     = models.IntegerField()
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)


class Profile(models.Model):
    
    # choice for gender
    GENDER = [
        ("male", "male"),
        ("female", "female"),
        ("other", "other")
    ]
    
    user_id         = models.ForeignKey() 
    contact_no      = models.CharField(max_length=16)
    profile_url     = models.TextField()
    date_of_birth   = models.DateField()
    gender          = models.CharField(choices = GENDER, default = None)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)


class Address(models.Model):
    profile_id  = models.ForeignKey(Profile, on_delete=models.CASCADE)
    country     = models.CharField(max_length=128, default=None)
    state       = models.CharField(max_length=128, default=None)
    district    = models.CharField(max_length=128, default=None)
    city        = models.CharField(max_length=128, default=None)
    streat      = models.CharField(max_length=128, default=None)
    colony      = models.CharField(max_length=128, default=None)
    house_no    = models.CharField(max_length=128, default=None)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)


class UserSalaryRecord(models.Model):
    user_id     = models.ForeignKey() # FK Auth_user table
    base_salary = models.IntegerField()
    created_at  = models.DateTimeField( auto_now_add=True )
    updated_at  = models.DateTimeField( auto_now=True )


class AppliedLeaves(models.Model):
    # choice for type_of_leave
    TYPE_OF_LEAVE = [
        ("L","L"),
        ("LOP","LOP"),
        ("HDL","HDL"),
    ]

    user_id         = models.ForeignKey() # FK Auth_user table
    date_of_applied = DateField()
    number_of_days  = IntegerField()
    type_of_leave   = CharField()
    status          = CharField()
    created_at      = models.DateTimeField( auto_now_add=True )
    updated_at      = models.DateTimeField( auto_now=True )


class Leaves(models.Model):
    user_id                 = models.ForeignKey() # FK Auth_user table
    paid_leave_balance      = models.IntegerField()
    unpaid_leaves_taken     = models.IntegerField()
    half_day_leaves_taken   = models.IntegerField()
    created_at              = models.DateTimeField( auto_now_add=True ) 
    updated_at              = models.DateTimeField( auto_now=True )


class Attendance(models.Model):

    # attendance status
    ATTENDANCE_STATUS = [
        ("P","P"),      # present
        ("A","A"),      # absent
        ("L","L"),      # leave
        ("HDL","HDl")   # half day leave
        ("LOP","LOP"),  # loss of Pay
    ]

    # choice for swipe status
    SWIPE_STATUS = [
        ("SignedIn","SignedIn"),
        ("SignedOut","SignedIOut"),
    ]
    
    user_id     = models.ForeignKey() # FK Auth_user table
    date        = models.DateField()
    attendance_status = models.CharField( choices = ATTENDANCE_STATUS )
    swipe_status = models.CharField( choices = SWIPE_STATUS )
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)


class Swipes(models.Model):
    
    # choice for swipe status
    SWIPE_STATUS = [
        ("SignedIn","SignedIn"),
        ("SignedOut","SignedIOut"),
    ]

    attendance_id = models.ForeignKey(Attendance)
    time = models.TimeField()
    swipe_status = models.CharField( choices = SWIPE_STATUS )
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)


class Post(models.Model):
    owner_user_id   = models.ForeignKey() # FK Auth_user table
    post_message    = models.TextField()
    content_url     = models.TextField()
    comment_count   = models.IntegerField()
    like_count      = models.IntegerField()
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post_id             = models.ForeignKey(Post, on_delete = models.CASCADE)
    commenter_user_id   = models.ForeignKey() # FK Auth_user table
    comment_message     = models.CharField(max_length=512)
    like_count          = models.IntegerField()
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
    

class Likes(models.Model):
    user_id     = models.ForeignKey() # FK Auth_user table
    post_id     = models.ForeignKey(Post, on_delete = models.CASCADE) 
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)


class CommentLike(models.Model):

    user_id = models.ForeignKey() # FK Auth_user table
    comment_id = models.ForeignKey(Comment)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)


