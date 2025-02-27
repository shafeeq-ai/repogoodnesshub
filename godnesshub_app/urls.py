from django.contrib import admin
from django.urls import path

from godnesshub_app.views import *

urlpatterns = [
    path('', LoginPage.as_view(), name="login2"),

    # /////////////////////////////////////// ADMIN ////////////////////////////////////////////

    path('view_complaint', ViewComplaint.as_view(), name="view_complaint"),
    
    path('feedbacks', Feedback.as_view(), name="feedbacks"),

    path('AddFoodinformation',Foodinformation.as_view(),name="AddFoodinformation"),

    path('DeleteFoodinformation/<int:id>',DeleteFoodinformation.as_view(),name='DeleteFoodinformation'),

    path('EditFoodinformation/<int:id>',EditFoodinformation.as_view(),name='EditFoodinformation'),

    path('notifications', Notification.as_view(), name="notifications"),

    path('main_page', MainPage.as_view(), name="main_page"),

    path('restuarant registration', restuarantregistration.as_view(), name="restuarant registration"),

    path('camp register', camp_register.as_view(), name="camp register"),

    path('viewandmanagefoodinfo', AddFoodinformation.as_view(), name="viewandmanagefoodinfo"),
    
    path('sendnotification', sendnotification.as_view(), name="sendnotification"),

    path('adminreply/<int:C_id>/',AdminReply.as_view(), name="adminreply"),

    path('logout',logout.as_view(), name="logout"),

    
    
    
    
    
    # ////////////////////////////////////// CAMP ///////////////////////////////////////////

    path('camp_homepage', camp_homepage.as_view(), name="camp_homepage"),
    
    path('campcomplaint', campcomplaint.as_view(), name="campcomplaint"),
    
    path('donation', donation.as_view(), name="donation"),
    
    path('send_request', send_request.as_view(), name="send_request"),

    path('working status', workingstatus.as_view(), name="working status"),

    path('foodinformation', foodinformation.as_view(), name="foodinformation"),


    #//////////////////////////////////restaurant////////////////////////////////////
    
    path('restaurant_home_page', restauranthomepage.as_view(), name="restaurant home page"),

    path('feedback', feedback.as_view(), name="feedback"),

    path('food information', foodinformation.as_view(), name="food information"),

    path('manage_profile', manageprofile.as_view(), name="manage profile"),

    path('notification', notification.as_view(), name="notification"),

    path('complaint', complaint.as_view(), name="complaint"),

    #////api////////////////////////////

    path('UserReg', UserReg.as_view(), name="UserReg"),

    path('LoginPageApi',LoginPageApi.as_view(), name="LoginPageApi"),

    path('foodinfoedit',foodinfoedit.as_view(), name="foodinfoedit"),

    path('FoodDetailsAPIView',FoodDetailsAPIView.as_view(), name="FoodDetailsAPIView"),
    path('FoodDetailsAPIView/<int:id>',FoodDetailsAPIView.as_view(), name="FoodDetailsAPIView"),


    path('items/', ItemTableAPIView.as_view()),
    path('items/<str:pk>/', ItemTableAPIView.as_view()),


    path('requests/', RequestTableAPIView.as_view(), name='request-list'),

    path('donations', DonationTableAPIView.as_view(), name='donation-list'),

    path('complaints/<int:lid>', ComplaintTableAPIView.as_view(), name='complaint-list'),
    path('AddItemApi/<int:lid>', AddItemApi.as_view(), name='AddItemApi'),
    # path('MedicalAccessoriesApi/', MedicalAccessoriesApi.as_view(), name='MedicalAccessoriesApi'),







]



    
