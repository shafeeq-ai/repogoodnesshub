from django.db import models

# Create your models here.
class LoginTable(models.Model):
    Username=models.CharField(max_length=100,blank=True,null=True)
    password=models.CharField(max_length=100,blank=True,null=True)
    Type=models.CharField(max_length=100,blank=True,null=True)

class UserTable(models.Model):
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    Name=models.CharField(max_length=100,blank=True,null=True)
    Age=models.IntegerField(blank=True,null=True)
    Address=models.CharField(max_length=100,blank=True,null=True)
    Phone=models.BigIntegerField(blank=True,null=True)
    Email=models.CharField(max_length=100,blank=True,null=True)


class CampTable(models.Model):
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    Name=models.CharField(max_length=100,blank=True,null=True)
    Camp_no=models.IntegerField(blank=True,null=True)
    Place=models.CharField(max_length=100,blank=True,null=True)
    Idproof=models.FileField(blank=True,null=True)
    Status=models.CharField(max_length=100,blank=True,null=True)
    Time=models.CharField(max_length=100,blank=True,null=True)
    Date=models.DateField(blank=True,null=True)
    


class ResturantTable(models.Model):
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    Name=models.CharField(max_length=100,blank=True,null=True)
    place=models.CharField(max_length=100,blank=True,null=True)
    Post=models.CharField(max_length=100,blank=True,null=True)
    Pin=models.IntegerField(blank=True,null=True)
    status=models.CharField(max_length=100,blank=True,null=True)
    Phone=models.BigIntegerField(blank=True,null=True)
    Email=models.CharField(max_length=100,blank=True,null=True)


class InformationTable(models.Model):
    category=models.CharField(max_length=100,blank=True,null=True)
    Info=models.CharField(max_length=100,blank=True,null=True)
    Date=models.DateField(auto_now_add=True, blank=True,null=True)


class feedbackTable(models.Model):
    USER=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    Feedback=models.CharField(max_length=100,blank=True,null=True)
    Rating=models.CharField(max_length=100,blank=True,null=True)
    Date=models.DateField(auto_now_add=True, blank=True,null=True)

class NotificationTable(models.Model):
    Notification=models.CharField(max_length=100,blank=True,null=True)
    Date=models.DateField(auto_now_add=True, blank=True,null=True)



class ItemTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True, blank=True)
    Item=models.CharField(max_length=100,blank=True,null=True)
    Category=models.CharField(max_length=100,blank=True,null=True)
    Image=models.FileField(blank=True,null=True)

class RequestTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable,on_delete=models.CASCADE, null=True, blank=True)
    Item=models.ForeignKey(ItemTable,on_delete=models.CASCADE,blank=True,null=True)
    Request=models.CharField(max_length=100,blank=True,null=True)
    Quantity=models.IntegerField(blank=True,null=True)
    Date=models.DateField(auto_now_add=True, blank=True,null=True)

class ComplaintTable(models.Model):
    LOGIN=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    Complaint=models.CharField(max_length=100,blank=True,null=True)
    Reply=models.CharField(max_length=100,blank=True,null=True)
    Date=models.DateField(auto_now_add=True, blank=True,null=True)

class DonationTable(models.Model):
    Username=models.CharField(max_length=100,blank=True,null=True)
    Item=models.CharField(max_length=100,blank=True,null=True)
    Submit=models.CharField(max_length=100,blank=True,null=True)
    Date=models.DateField(blank=True,null=True)
    Category=models.CharField(max_length=100,blank=True,null=True)
    

   

class fooddetails(models.Model):
    RESTID=models.ForeignKey(ResturantTable,on_delete=models.CASCADE,blank=True,null=True)
    foodcategory=models.CharField(max_length=100,blank=True,null=True)
    food_status=models.CharField(max_length=100,blank=True,null=True)
    food_name=models.CharField(max_length=100,blank=True,null=True)
    about=models.CharField(max_length=100,blank=True,null=True)

                
       
