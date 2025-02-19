
from rest_framework.serializers import ModelSerializer
from godnesshub_app.models import *


class LoginSerializer(ModelSerializer):  
    class Meta:
        model = LoginTable
        fields = ['Username', 'password']

class UserSerializer(ModelSerializer):
    class Meta:
        model = UserTable
        fields = ['Name', 'Age', 'Address', 'Phone', 'Email']

class RestaurantSerializer(ModelSerializer):  
    class Meta:
        model = ResturantTable
        fields = ['Name', 'place', 'Post', 'Pin', 'Phone', 'Email']

class fooddetailsSerializer(ModelSerializer):  
    class Meta:
        model = fooddetails
        fields = ['foodcategory', 'food_status','food_name','about']


class ItemTableSerializer(ModelSerializer):  
    class Meta:
        model = ItemTable
        fields = ['Item', 'Category','Image']

class requestSerializer(ModelSerializer):  
    class Meta:
        model = RequestTable
        fields = ['Item', 'Request','Quantity','Date']


class ComplaintTableSerializer(ModelSerializer):  
    class Meta:
        model = ComplaintTable
        fields = ['Complaint', 'Reply','Date']

class feedbackSerializer(ModelSerializer):  
    class Meta:
        model = feedbackTable
        fields = ['Feedback','Rating','Date']


class DonationTableSerializer(ModelSerializer):
    class Meta:
        model = DonationTable
        fields = '__all__'