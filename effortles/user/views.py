from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Department, Designation

User = get_user_model()

# Create your views here.
class EmployeeRegisterView(CreateView):
    

    def post(self, request):
        user_first_name = request.POST['FirstNameInp']
        user_last_name = request.POST['LastNameInp']
        user_email = request.POST['EmailInp']
        user_type = request.POST['TypeInp']
        user_joining_date = request.POST['JoiningDateInp']

        user = User.objects.filter( email = user_email )

        if(len(user)!=0):
            return HttpResponse("email already taken")
        else:

            user_entry = User()
            user_entry.password = "_"
            user_entry.user_name = user_email
            user_entry.first_name = user_first_name
            user_entry.last_name = user_last_name
            user_entry.email = user_email
            user_entry.is_staff = 1
            user_entry.is_active = 1
            user_entry.date_joined = user_joining_date
            user_entry.type = user_type
            user_entry.department_id = Department(1)
            user_entry.designation_id = Designation(1) 
            user_entry.save()
            



        #     return redirect("/login/{}".format(user.id))
            
        # else:
        #     return HttpResponse("wrong credential")

        return HttpResponse(user_first_name+" "+user_last_name+" "+user_email+" "+user_type+" "+user_joining_date)
        
