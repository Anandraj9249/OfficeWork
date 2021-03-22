from django.urls import path
from RoleApp import views
from .views import Index
from .views import Dashboard
from .views import Register
from .views import Login
from .views import UserList
# from .views import permission
# from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', Index.as_view(), name="Home"),
    path('admin/dashboard', Dashboard.as_view(), name="Dashboard"),
    path('admin/Register', Register.as_view(), name="Register"),
    path('admin/Login', Login.as_view(), name="Login"),
    path('admin/UserList', UserList.as_view(), name="UserList"),
    # path('delete/<int:id>', views.destroy),
    # path('edit/<int:id>', views.edit),
    # path('update/<int:id>', views.edit),  
    # path('permission',permission.as_view() , name="Permission"),
    # path('load_CSC', views.load_CSC, name='ajax_load_cities')  

]
