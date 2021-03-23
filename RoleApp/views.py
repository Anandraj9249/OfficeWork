from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import HttpResponseRedirect
from django.shortcuts import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import CustomUser
from django.contrib import messages
from django.views import View
# from django.contrib.auth.forms import UserCreationForm

# from django.contrib.auth.models import User
# Create your views here.

# def CreateUser(request):
#     if request.method == 'POST':
#         fm = UserCreationForm(request.POST)
#         if fm.is_valid():
#             fm.save()
#     else:
#         fm = UserCreationForm()
#     return render(request, 'AdminPage/UserCreation.html', {'form': fm})

class Index(View):
    def get(self , request):
        return render(request, 'AdminPage/index.html')

class Dashboard(View):
    def get(self , request):
        return render(request, 'Public/Dashboard.html')

class CreateUser(View):
    # Get form
    def get(self , request):
        return render(request, 'AdminPage/AddUsers.html')
    def post(self , request):
        # Creating the user 
        postData = request.POST
        username = postData.get('username')
        first_name = postData.get('first_name')
        mid_name = postData.get('mid_name')
        last_name = postData.get('last_name')
        email = postData.get('email')
        phone = postData.get('phone')
        dob = postData.get('dob')
        password = postData.get('password')
        Cname = postData.get('Cname')
        Sname = postData.get('Sname')
        city = postData.get('city')
        # value already feel after find error
        value = {
            'username':username , 
            'first_name':first_name , 
            'mid_name':mid_name , 
            'last_name':last_name , 
            'email=email':email , 
            'phone':phone , 
            'dob':dob , 
            'password':password , 
            'Cname':Cname,
            'Sname':Sname, 
            'city':city , 
        }
         #e nd value already feel after find error
        error_message = None
        # Saving Data 
        user = CustomUser( 
                        first_name=first_name , 
                        mid_name=mid_name , 
                        last_name=last_name , 
                        email=email , 
                        phone=phone , 
                        dob=dob , 
                        password=password , 
                        Cname=Cname ,
                        Sname=Sname ,
                        city=city ,) 

        # End Saving data
        # Check Validation 
        # if not username.isalnum():
        #     error_message = "User name should only contain letters and numbers"
        # if len(username) <6:
        #     error_message = "Your user name must be under 10 characters"
        if(not first_name):
            error_message = "First Name Required !!"
        elif len(first_name) < 4:
            error_message = "First Name must be 4 Char long"
        if(not mid_name):
            error_message = "Middlen Name Required !!"
        elif len(mid_name) < 4:
            error_message = "Middle Name must be 4 Char Long"
        if len(phone) <10:
            error_message = "Phone Number Must be 10 Digit Long"
        if len(password) > 10:
            error_message = "Password must be under 10 digit long"
        elif user.isExixts():
            error_message = "Email Already register"
        # End Validation
        if not error_message:
            user.set_password(password)
            # # # the Hasher Password
            # user.password = make_password(user.password)
            # # #End Hasher Password
            user.register() #Save and End The Creating User
            return redirect('UserList')
        else:
            # Create Key 
            data ={
                 'error':error_message,
                 'values':value
                 }
                 #values': value'''
            # End Key
            return render(request, 'AdminPage/AddUsers.html',data)
        return redirect('UserList')


class AdminLogin(View):
    #Hold The Return URL
    return_url = None
    def get(self , request):
        AdminLogin.return_url = request.GET.get('return_url')
        return render(request, 'AdminPage/login.html')
    def post(self , request):
        if request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = CustomUser.get_user_by_email(email)
            error_message = None
            if user:
                flag = check_password(password , user.password) #Decode The Password
                if flag:
                    # Save the object of user in session
                    request.session['user_id'] = user.id
                    request.session['user_email'] = user.email
                    # Create Return URL 
                    if AdminLogin.return_url:
                        return HttpResponseRedirect(AdminLogin.return_url)
                    else:
                        AdminLogin.return_url = None
                        return redirect('Dashboard')
                else:
                    error_message = " Invalid Credentials !!"
            else:
                error_message = " Invalid Credentials !!"
            return render(request, 'AdminPage/login.html', {'error':error_message})

class UserList(View):
    def get(self , request):
        user = CustomUser.objects.all()
        return render(request, 'AdminPage/UserList.html', {'user' : user})
def edit(request, id):  
    users = CustomUser.objects.get(id=id) 
    data = {
        'users': users,
    } 
    return render(request,'AdminPage/Edit.html', data)

def update(request, id):
    users = CustomUser.object.get(id=id)
    return render(request,'AdminPage/Edit.html')

def destroy(request, id):  
    users = Users.objects.get(id=id)  
    users.delete()  
    return redirect("/UserList") 

class permission(View):
    def get(self , request):  
        get_user = CustomUser.objects.all()
        return render(request, 'AdminPage/permission.html', {'get_user': get_user})