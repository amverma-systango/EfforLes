from django.db import models
from django.conf import settings



class Attendance(models.Model):

    ATTENDANCE_STATUS = [
        ("Present","Present"),      
        ("Absent","Absent"),      
        ("Leave","Leave"),      
        ("Half Day Leave","HalfDayLeave"),
        ("Loss Of Pay","LossOfPay"),  
    ]

    SWIPE_STATUS = [
        ("SignedIn","SignedIn"),
        ("SignedOut","SignedOut"),
    ]
    
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    date = models.DateField()
    attendance_status = models.CharField(max_length=15, choices=ATTENDANCE_STATUS)
    swipe_status = models.CharField(max_length=10, choices=SWIPE_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user_id)+" "+str(self.date)


class Swipe(models.Model):
    
    SWIPE_STATUS = [
        ("SignedIn","SignedIn"),
        ("SignedOut","SignedOut"),
    ]

    attendance_id = models.ForeignKey(Attendance, on_delete= models.CASCADE) 
    time = models.TimeField()
    swipe_status = models.CharField(max_length=10, choices=SWIPE_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.attendance_id)

