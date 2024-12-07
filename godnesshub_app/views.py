from django.shortcuts import render
from django.views import View

from .models import LoginTable
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .form import *
from .models import LoginTable





# Create your views here.

class LoginPage(View):
    def get(self, request):
        return render(request, "administration/login.html")
    def post(self,request):
        username = request.POST['username']
        password = request.POST['password']
        login_obj= LoginTable.objects.get(Username=username, password=password)
        if login_obj.Type =="admin":
            return HttpResponse('''<script>alert("welcome to admin home");window.location="/main_page"</script>''')
        if login_obj.Type =="restaurant":
            return HttpResponse('''<script>alert("welcome to RESTAURANT home");window.location="/restaurant_home_page"</script>''')
        if login_obj.Type =="Camptable":
            return HttpResponse('''<script>alert("welcome to camp home");window.location="/camp_homepage"</script>''')
        else:
            return HttpResponse('''<script>alert("invalid");window.location="/"</script>''')


# /////////////////////////////////////////////////// ADMIN //////////////////////////////////////



class ViewComplaint(View):
    def get(self, request):
        return render(request, "administration/complaint.html")
    
class Feedback(View):
    def get(self, request):
        return render(request, "administration/feedback.html")

class Foodinformation(View):
    def get(self, request):
        obj=fooddetails.objects.all()
        return render(request,"administration/viewandmanagefoodinfo.html",{'val':obj})
    
class AddFoodinformation(View):
    def get(self, request):
        return render(request, "administration/food information.html")

    def post(self, request):
     print("jj")
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
        return render(request, "administration/notification.html")

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

class complaint(View):
    def get(self, request):
        return render(request, "camp\complaint.html")
    
class donation(View):
    def get(self, request):
        return render(request, "camp\donation.html")

class manage(View):
    def get(self, request):
        return render(request, "camp\manage.html")

class medical(View):
    def get(self, request):
        return render(request, "camp\medical.html")

class foodinformation(View):
    def get(self, request):
        return render(request, "camp\food information.html")

    
class request(View):
    def get(self, request):
        return render(request, "camp/request.html")
    
class workingstatus(View):
    def get(self, request):
        return render(request, "camp/working status.html")

#/////////////////////////////restaurant////////////////////////

class restauranthomepage(View):
    def get(self, request):
        return render(request, "restaurant/restaurant home page.html")

class feedback(View):
    def get(self, request):
        return render(request, "restaurant/feedback.html")

class foodinformation(View):
    def get(self, request):
        return render(request, "restaurant/food information.html")

class manageprofile(View):
    def get(self, request):
        return render(request, "restaurant/manage profile.html")
  
class notification(View):
    def get(self, request):
        return render(request, "restaurant/notification.html")
    
class complaint(View):
    def get(self, request):
        return render(request, "restaurant/complaint.html")
    

    

    


    