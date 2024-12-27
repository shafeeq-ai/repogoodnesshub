from django import forms
from .models import *

class RestaurantForm(forms.ModelForm):  
    class Meta:
        model = ResturantTable
        fields = ['Name', 'place', 'Post', 'Pin', 'Phone', 'Email']

class CampForm(forms.ModelForm):  
    class Meta:
        model = CampTable
        fields= ['Name','Camp_no','Place','Idproof']


class addfoodform(forms.ModelForm):
    class Meta:
        model = fooddetails
        fields = ['foodcategory','food_status','food_name','about']

class updatefoodform(forms.ModelForm):
    class Meta:
        model = fooddetails
        fields = ['foodcategory','food_status','food_name','about']

class notificationform(forms.ModelForm):
    class Meta:
        model = NotificationTable
        fields = ['Notification']

class adminreplyform(forms.ModelForm):
        class Meta:
            model = ComplaintTable
            fields = ['Reply']


class restcomplaintform(forms.ModelForm):
        class Meta:
            model = ComplaintTable
            fields = ['Complaint']

class requestform(forms.ModelForm):
         class Meta:
            model = RequestTable
            fields = ['Item','Request','Quantity']

class StatusForm(forms.ModelForm):
         class Meta:
            model =CampTable
            fields = ['Status','Time','Date']
