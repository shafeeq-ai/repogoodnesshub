from django.shortcuts import get_object_or_404, render
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

class logout(View):
     def get(self, request):
            return HttpResponse('''<script>alert("logout succesfully");window.location="/"</script>''')



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
        obj=DonationTable.objects.all()
        return render(request, "camp\donation.html",{'val':obj})

class manage(View):
    def get(self, request):
        return render(request, "camp\manage.html")

class send_request(View):
    def get(self, request):
        return render(request, "camp/send_request.html")

    def post(self, request):
        print("Received FILES:", request.FILES)  # Debugging: Check if image file is received
        form = requestform(request.POST, request.FILES)  

        if form.is_valid():
            request_instance = form.save(commit=False)
            obj = LoginTable.objects.get(id=request.session.get('lid'))
            request_instance.LOGIN = obj

            print("Before Saving - Image:", request_instance.Image)  # Debugging
            request_instance.save()
            print("After Saving - Image:", request_instance.Image)  # Debugging

            return HttpResponse('''<script>alert("Request sent");window.location="/camp_homepage"</script>''')
        else:
            print("Form errors:", form.errors)  # Debugging: Check if form validation fails

        return HttpResponse("Form submission failed")



    
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


# ///////////////////////////////////////////////////// API ////////////////////////////////////////
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from godnesshub_app.serializer import *
class UserReg(APIView):
    def post(self,request):
        print("#############",request.data)
        User_serial = UserSerializer(data=request.data)
        login_serial = LoginSerializer(data=request.data)
        data_valid = User_serial.is_valid()
        login_valid = login_serial.is_valid()
        print("#############",data_valid,login_valid)
        if data_valid and login_valid:
            print("&&&&&&&&&&&&&&&&&&&&&")
            password = request.data['password']
            login_profile = login_serial.save(Type='USER', password=password)
            User_serial.save(LOGINID=login_profile)
            return Response(User_serial.data, status=status.HTTP_201_CREATED)
        return Response({'login_error' :login_serial.errors if not login_valid else None,
                       'user_error': User_serial.errors if not data_valid else None}, status=status.HTTP_400_BAD_REQUEST)


class LoginPageApi(APIView):
    def post(self, request):
        response_dict = {}

        # Get data from the request
        username = request.data.get("username")
        password = request.data.get("password")

        # Validate input
        if not username or not password:
            response_dict["message"] = "failed"
            return Response(response_dict, status=HTTP_400_BAD_REQUEST)

        # Fetch the user from LoginTable
        t_user = LoginTable.objects.filter(Username=username).first()

        if not t_user:
            response_dict["message"] = "failed"
            return Response(response_dict, status=status.HTTP_401_UNAUTHORIZED)


        # Successful login response
        response_dict["message"] = "success"
        response_dict["login_id"] = t_user.id
        response_dict["type"] = t_user.Type 

        return Response(response_dict, status=status.HTTP_200_OK)

class foodinfoedit(APIView):
    def get(self, request):
        foodinfotable = foodinfotable.objects.all()
        foodinfotable_serializer = foodinfotable(foodinfotable, many = True)
        print("-------------> Offer images", foodinfotable)
        return Response(foodinfotable_serializer.data)


# API View
class FoodDetailsAPIView(APIView):
    
    def get(self, request, pk=None):
        if pk:
            food = get_object_or_404(fooddetails, pk=pk)
            serializer = FoodDetailsSerializer(food)
        else:
            food = fooddetails.objects.all()
            serializer = fooddetailsSerializer(food, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        print(request.data)
        serializer = fooddetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        food = get_object_or_404(fooddetails, pk=pk)
        serializer = fooddetailsSerializer(food, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    


from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import ItemTable


class ItemTableAPIView(APIView):
    def get(self, request, pk=None):
        print("-------------> Requested Category:", pk)

        if pk:
            # Normalize category input
            category = pk.lower()

            if category in ["clothes", "medical_accessories"]:
                items = ItemTable.objects.filter(Category__iexact=category)

                print(f"-------------> Found {items.count()} items for category: {category}")
                for item in items:
                    print(f"Item: {item.Item}, Category: {item.Category}, Image: {item.Image}")

                if items.exists():
                    serializer = ItemTableSerializer(items, many=True)

                    # Convert response to ensure all fields are strings (to avoid Flutter type issues)
                    response_data = [
                        {
                            "Item": str(item["Item"]) if item["Item"] else "",
                            "Category": str(item["Category"]) if item["Category"] else "",
                            "Image": str(item["Image"]) if item["Image"] else "",
                        }
                        for item in serializer.data
                    ]

                    return Response(response_data, status=status.HTTP_200_OK)

                return Response({"message": "No items found for this category"}, status=status.HTTP_404_NOT_FOUND)

            return Response({"message": "Invalid category"}, status=status.HTTP_400_BAD_REQUEST)

        # If no pk is provided, return all items
        items = ItemTable.objects.all()
        serializer = ItemTableSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class RequestTableAPIView(APIView):
    
    def get(self, request):
        requests = RequestTable.objects.all()
        serializer = requestSerializer(requests, many=True)
        print('------------->', serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        serializer = requestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class MedicalAccessoriesApi(APIView):
#     def get(self, request):
#         donations = ItemTable.objects.filter
#         serializer = ItemTableSerializer(donations, many=True)
#         print("--------->", serializer.data)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
class DonationTableAPIView(APIView):
    def get(self, request):
        donations = DonationTable.objects.all()
        serializer = DonationTableSerializer(donations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data.copy()
        user_id = data.get("lid")  # Extract `lid` (LoginTable ID)
        
        if user_id:
            try:
                user = LoginTable.objects.get(id=user_id)
                data["Username"] = user.id  # Assign to ForeignKey field
            except LoginTable.DoesNotExist:
                return Response({"error": "Invalid User ID"}, status=status.HTTP_400_BAD_REQUEST)

        # Auto-fill the Date field if not provided
        if not data.get("Date"):
            data["Date"] = datetime.date.today()

        serializer = DonationTableSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ComplaintTableAPIView(APIView):
    def get(self, request, lid):
        complaints = ComplaintTable.objects.all()
        serializer = ComplaintTableSerializer(complaints, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, lid):
        print("---------->", request.data)
        obj=LoginTable.objects.get(id=lid)
        comp_obj = ComplaintTable()
        comp_obj.LOGIN = obj
        comp_obj.Complaint = request.data.get('complaint')
        comp_obj.Reply = request.data.get('Reply')
        comp_obj.save()
        return Response(status=status.HTTP_201_CREATED)
    
class AddItemApi(APIView):
    # def get(self, request, lid):
    #     complaints = ComplaintTable.objects.all()
    #     serializer = ComplaintTableSerializer(complaints, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, lid):
        print("---------->", request.data)
        obj=LoginTable.objects.get(id=lid)
        comp_obj = ItemTable()
        comp_obj.LOGIN = obj
        comp_obj.Item = request.data.get('name')
        comp_obj.Category = request.data.get('category')
        comp_obj.Quantity = request.data.get('quantity')
        comp_obj.Image = request.data.get('image')
        comp_obj.save()
        return Response(status=status.HTTP_201_CREATED)
