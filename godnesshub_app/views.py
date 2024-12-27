from django.shortcuts import render
from django.views import View

from .models import LoginTable
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .form import *
from django.utils import timezone
from .models import *





# Create your views here.

class LoginPage(View):
    def get(self, request):
        return render(request, "administration/login.html")
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        login_obj= LoginTable.objects.get(Username=username, password=password)
        request.session['lid']=login_obj.id
        if login_obj.Type =="admin":
            return HttpResponse('''<script>alert("welcome to admin home");window.location="/main_page"</script>''')
        if login_obj.Type =="restaurant":
            return HttpResponse('''<script>alert("welcome to RESTAURANT home");window.location="/restaurant_home_page"</script>''')
        if login_obj.Type =="Camptable":
            return HttpResponse('''<script>alert("welcome to camp home");window.location="/camp_homepage"</script>''')
        else:
            return HttpResponse('''<script>alert("invalid");window.location="/"</script>''')


# /////////////////////////////////////////////////// ADMIN //////////////////////////////////////

class sendnotification(View):
    def get(self, request):
        return render(request, "administration/sendnotification.html")
    def post(self,request):
        form=notificationform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("Notification sent");window.location="/notifications"</script>''')
    
    

class ViewComplaint(View):
    def get(self, request):
        obj=ComplaintTable.objects.all()
        return render(request, "administration/complaint.html",{'val':obj})

class AdminReply(View):
    def get(self, request,C_id):
        obj=ComplaintTable.objects.get(id=C_id)
        print(obj)
        return render(request, "administration/adminreply.html")
    def post(self,request,C_id):
        obj=ComplaintTable.objects.get(id=C_id)
        form=adminreplyform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return HttpResponse('''<script>alert("reply sent");window.location="/view_complaint"</script>''')
        

class Feedback(View):
    def get(self, request):
        obj=feedbackTable.objects.all()
        return render(request, "administration/feedback.html",{'val':obj})

class Foodinformation(View):
    def get(self, request):
        obj=fooddetails.objects.all()
        return render(request,"administration/viewandmanagefoodinfo.html",{'val':obj})
    
class AddFoodinformation(View):
    def get(self, request):
        return render(request, "administration/food information.html")

    def post(self, request):
     form=addfoodform(request.POST)
     if form.is_valid():
      form.save()
     return HttpResponse('''<script>alert("food information added");window.location="/AddFoodinformation"</script>''')

class DeleteFoodinformation(View):
    def get(self, request,id):
        obj= fooddetails.objects.get(id=id)
        obj.delete()
        return HttpResponse('''<script>alert("food information deleted successfully");window.location="/AddFoodinformation"</script>''')

class EditFoodinformation(View):
    def get(self, request,id):
      obj= fooddetails.objects.get(id=id)
      return render(request,"administration/foodinfoedit.html",{'val':obj})

    def post(self, request,id):
        obj= fooddetails.objects.get(id=id)
        form=updatefoodform(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return HttpResponse('''<script>alert("food information updated");window.location="/AddFoodinformation"</script>''')



        

   
# class addfoodinformation(view):
    # def get(self,request):
    #      return render(request, "administration/food information.html")


class Notification(View):
    def get(self, request):
         obj=NotificationTable.objects.all()
         return render(request, "administration/notification.html",{'val':obj})

class restuarantregistration(View):
    def get(self, request):
        return render(request, "administration/restaurant registraion.html")
    def post(self, request):
        form = RestaurantForm(request.POST)
        
        if form.is_valid():
        
           
            login_instance = LoginTable.objects.create(
                Type='restaurant',
                Username=request.POST['Username'],
                password=request.POST['password']  # Corrected the typo here
            )

            # Save the restaurant registration details with reference to the created user
            reg_form = form.save(commit=False)
            reg_form.LOGINID = login_instance  # Link to the created user
            reg_form.save()

            return HttpResponse('''<script>alert("Registered successfully!"); window.location="/main_page"</script>''')

        # If form is not valid, send back an error response
        return HttpResponse('''<script>alert("Form submission failed! Please check the fields and try again."); window.location="/"</script>''')

    
class MainPage(View):
    def get(self, request):
        return render(request, "administration\MAIN PAGE.html")
    
class camp_register(View):
    def get(self, request):
        return render(request, "administration/camp_register.html")

    def post(self, request):
        print("abc")
        form = CampForm(request.POST,request.FILES)
        if form.is_valid():
            reg_form = form.save(commit=False)
           
            login_instance = LoginTable.objects.create(
                Type='Camptable',
                Username=request.POST['Username'],
                password=request.POST['password']  # Corrected the typo here
            )

            # Save the restaurant registration details with reference to the created user
            
            reg_form.LOGINID = login_instance  # Link to the created user
            reg_form.save()

            return HttpResponse('''<script>alert("Registered successfully!"); window.location="/main_page"</script>''')

        # If form is not valid, send back an error response
        return HttpResponse('''<script>alert("Form submission failed! Please check the fields and try again."); window.location="/camp_homepage"</script>''')


        

#//////////////////////////////////////////camp////////////////////////////////

class camp_homepage(View):
    def get(self, request):
        return render(request, "camp\camp_homepage.html")

class campcomplaint(View):
    def get(self, request):
        obj=ComplaintTable.objects.all()
        return render(request, "camp\campcomplaint.html",{'val':obj})
            
class donation(View):
    def get(self, request):
        obj=ComplaintTable.objects.all()
        return render(request, "camp\donation.html",{'val':obj})

class manage(View):
    def get(self, request):
        return render(request, "camp\manage.html")

class send_request(View):
    def get(self, request):
        return render(request, "camp\send_request.html")
    def post(self,request):
        form=requestform(request.POST)
        if form.is_valid():
            request_instance=form.save(commit=False)
            print(request.session.get('lid'))
            obj=LoginTable.objects.get(id=request.session.get('lid'))
            request_instance.LOGIN=obj
            request_instance.save()
            return HttpResponse('''<script>alert("Request sented");window.location="/camp_homepage"</script>''')
    
class workingstatus(View):
    def get(self, request):
        return render(request, "camp/working status.html")

    def post(self, request):
        # Assuming login_obj.id is stored in the session
        login_id = request.session.get('lid')

        # Ensure the login_id is valid
        if login_id:
            try:
                # Fetch the LoginTable object using the stored login ID
                login_obj = LoginTable.objects.get(id=login_id)

                # Fetch the existing CampTable entry that corresponds to this login ID
                camp = CampTable.objects.filter(LOGINID=login_obj).first()

                # Check if we have a valid camp associated with the login
                if camp:
                    # Process the form data
                    form = StatusForm(request.POST)

                    if form.is_valid():
                        # Update the existing CampTable entry
                        camp.Status = form.cleaned_data['Status']  # Update status
                        camp.Time = timezone.now().strftime('%H:%M:%S')  # Set the current time
                        camp.Date = form.cleaned_data['Date']  # Update the date from the form
                        
                        # Save the updated camp record
                        camp.save()

                        # Redirect or provide a success response
                        return HttpResponse('''<script>alert("Status Updated");window.location="/camp_homepage"</script>''')

            except LoginTable.DoesNotExist:
                return HttpResponse('Error: Invalid login ID.')

        return HttpResponse('Error: Login session expired or invalid.')
    

# class foodinformation(View):
#     def get(self, request):
#         return render(request, "camp\food information.html")

    
# class request(View):
#     def get(self, request):
#         return render(request, "camp/request.html")
    


#/////////////////////////////restaurant////////////////////////

class restauranthomepage(View):
    def get(self, request):
        return render(request, "restaurant/restaurant home page.html")

class feedback(View):
    def get(self, request):
        obj=feedbackTable.objects.all()
        return render(request, "restaurant/feedback.html",{'val':obj}) 

class foodinformation(View):
    def get(self, request):
        return render(request, "restaurant/food information.html")

class manageprofile(View):
    def get(self, request):
        obj=ResturantTable.objects.get(LOGINID__id=request.session['lid'])
        return render(request, "restaurant/manage profile.html",{'val':obj})
    def post(self, request):
        obj=ResturantTable.objects.get(LOGINID__id=request.session['lid'])
        form=RestaurantForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return HttpResponse('''<script>alert("Information updated");window.location="/restaurant_home_page"</script>''')

    
class notification(View):
    def get(self, request):
        c=NotificationTable.objects.all()
        return render(request, "restaurant/notification.html", {'a':c})
    
class complaint(View):
    def get(self, request):
        return render(request, "restaurant/complaint.html")
    

    

    


    