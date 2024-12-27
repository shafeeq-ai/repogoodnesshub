from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(LoginTable)
admin.site.register(UserTable)
admin.site.register(CampTable)
admin.site.register(ResturantTable)
admin.site.register(InformationTable)
admin.site.register(feedbackTable)
admin.site.register(NotificationTable)
admin.site.register(ItemTable)
admin.site.register(RequestTable)
admin.site.register(ComplaintTable)
admin.site.register(DonationTable)

admin.site.register(fooddetails)