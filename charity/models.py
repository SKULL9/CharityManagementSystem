from django.db import models
from django.contrib.auth.models import User



class Donor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact =models.CharField(max_length=15,null=True)
    address =models.CharField(max_length=300,null=True)
    userpic =models.FileField(null=True)
    regdate =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

class Volunteer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact =models.CharField(max_length=15,null=True)
    address =models.CharField(max_length=300,null=True)
    userpic =models.FileField(null=True)
    idpic =models.FileField(null=True)
    aboutme =models.CharField(max_length=300,null=True)
    status =models.CharField(max_length=20,null=True)
    regdate =models.DateTimeField(auto_now_add=True)
    adminremark =models.CharField(max_length=20,null=True)
    updationdate=models.DateField(null=True)
    def __str__(self):
        return self.user.username

class DonationArea(models.Model):
    areaname =models.CharField(max_length=100,null=True)
    description =models.CharField(max_length=300,null=True)
    creationdate =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.areaname

class Donation(models.Model):
    donor = models.ForeignKey(Donor,on_delete=models.CASCADE)
    donationname = models.CharField(max_length=100,null=True)
    donationpic = models.FileField(null=True)
    collectionloc = models.CharField(max_length=300, null=True)
    description = models.CharField(max_length=300,null=True)
    status = models.CharField(max_length=50,default="pending")
    donationdate = models.DateTimeField(auto_now_add=True)
    adminremark = models.CharField(max_length=300,null=True,default="something")
    volunteer = models.ForeignKey(Volunteer,on_delete=models.CASCADE,default="1")
    donationarea = models.ForeignKey(DonationArea, on_delete=models.CASCADE,default="1")
    volunteerremark = models.CharField(max_length=300,null=True,default="something")


    def __str__(self):
        return self.donationname

class Gallery(models.Model):
    donation = models.ForeignKey(Donation,on_delete=models.CASCADE)
    deliverypic = models.FileField(null=True)
    creationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.donation.donationname