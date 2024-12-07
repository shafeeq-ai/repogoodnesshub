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
    
    
    # ////////////////////////////////////// CAMP ///////////////////////////////////////////

    path('camp_homepage', camp_homepage.as_view(), name="camp_homepage"),
    
    path('complaint', complaint.as_view(), name="complaint"),
    
    path('donation', donation.as_view(), name="donation"),
    
    path('manage', manage.as_view(), name="manage"),

    path('medical', medical.as_view(), name="medical"),


    path('request', request.as_view(), name="request"),

    path('working status', workingstatus.as_view(), name="working status"),

    path('foodinformation', foodinformation.as_view(), name="foodinformation"),


    #//////////////////////////////////restaurant////////////////////////////////////
    
    path('restaurant_home_page', restauranthomepage.as_view(), name="restaurant home page"),

    path('feedback', feedback.as_view(), name="feedback"),

    path('food information', foodinformation.as_view(), name="food information"),

    path('manage profile', manageprofile.as_view(), name="manage profile"),

    path('notification', notification.as_view(), name="notification"),

    path('complaint', complaint.as_view(), name="complaint"),

    

]




