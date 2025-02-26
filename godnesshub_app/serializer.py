
import datetime
from rest_framework.serializers import ModelSerializer
from godnesshub_app.models import *
from rest_framework import serializers

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
    name=serializers.CharField(source='Item.Item', read_only=True)  
    class Meta:
        model = RequestTable
        fields = ['Item','Date','status', 'name','Image']


class ComplaintTableSerializer(ModelSerializer):  
    class Meta:
        model = ComplaintTable
        fields = ['Complaint', 'Reply','Date']

class feedbackSerializer(ModelSerializer):  
    class Meta:
        model = feedbackTable
        fields = ['Feedback','Rating','Date']


class DonationTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationTable
        fields = '__all__'

    def create(self, validated_data):
        # Get the user instance from the provided `lid`
        user_id = self.initial_data.get("lid")  # Assuming "lid" is sent in the request
        user = LoginTable.objects.get(id=user_id)  # Fetch the user instance

        # Create the donation entry with the user and the provided amount
        donation = DonationTable.objects.create(
            Username=user,
            Amount=validated_data.get("Amount"),
            Date=datetime.date.today()  # Auto-assign today's date
        )
        return donation
