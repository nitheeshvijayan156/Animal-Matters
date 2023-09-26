from email.headerregistry import Address
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserAccounts(AbstractUser):
    mobile_number = models.CharField(max_length=10)

class Report(models.Model):
    report_location = models.TextField()
    report_description = models.TextField()
    report_file = models.FileField()
    status = models.CharField(max_length=100)
    report_resolution = models.TextField()
    created_by = models.ForeignKey(UserAccounts,on_delete=models.PROTECT)
    report_handler = models.ForeignKey(UserAccounts,on_delete=models.PROTECT,related_name="report_handler")
    resolved_on = models.DateTimeField()
    created_on = models.DateTimeField()

class UaerOtpInstance(models.Model):
    user_instance = models.ForeignKey(UserAccounts,on_delete=models.CASCADE)
    generated_otp = models.CharField(max_length=10)