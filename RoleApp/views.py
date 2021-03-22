from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponse
from .models import CustomUser
from django.contrib import messages
# from django.contrib.auth.models import User
from django.views import View
# Create your views here.
class Index(View):
    def get(self , request):
        return render(request, 'AdminPage/index.html')

class Dashboard(View):
    def get(self , request):
        return render(request, 'Public/Dashboard.html')
    def post(self , request):
        pass


class Register(View):
    def get(self , request):
        return render(request, 'AdminPage/Register.html')

    def post(self , request):
        # Creating the user 
        postData = request.POST
        first_name = postData.get('first_name')
        mid_name = postData.get('mid_name')
        last_name = postData.get('last_name')
        email = postData.get('email')
        phone = postData.get('phone')
        dob = postData.get('dob')
        password = postData.get('password')
        city = postData.get('city')
        country = postData.get('country')
        #Validation
        '''value = {
            'username':username , 
            'first_name':first_name , 
            'mid_name':mid_name , 
            'last_name':last_name , 
            email=email , 
            phone=phone , 
            dob=dob , 
            password=password , 
            city=city , 
            country=country 
        }'''
        error_message = None
        user = CustomUser( 
                        first_name=first_name , 
                        mid_name=mid_name , 
                        last_name=last_name , 
                        email=email , 
                        phone=phone , 
                        dob=dob , 
                        password=password , 
                        city=city , 
                        country=country ,)
        if(not first_name):
            error_message = "First Name Required !!"
        elif len(first_name) < 4:
            error_message = "First Name must be 4 Char long"
        elif user.isExixts():
            error_message = "Email Already register"
            
        if not error_message:
            # # encode the Hasher Password
            # user.password = make_password(user.password)
            # #End Hasher Password
            user.register() #Save and End The Creating User
            return redirect('/admin/UserList')
        else:
            data ={
                 'error':error_message,
                 }
                 #values': value'''
            return render(request, 'AdminPage/CreateUser.html',data)
        return redirect('/UserList')


class Login(View):
    def get(self , request):
        return render(request, 'AdminPage/AdminLogin.html')

class UserList(View):
    def get(self , request):
        return render(request, 'AdminPage/UserList.html')