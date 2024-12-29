from django.urls import path
from . import views

urlpatterns = [ 
    path('HomePage', views.HomePage, name='HomePage'),
    path("",views.SignIn,name="SignIn"),
    path("AdminIndex",views.AdminIndex,name="AdminIndex"),  
    path("LandOwnerIndex",views.LandOwnerIndex,name="LandOwnerIndex"),  
    path("SignUp",views.SignUp,name="SignUp"),
    path("SignOut",views.SignOut,name="SignOut"),
    path("user_admin",views.user_admin,name="user_admin"),
    path("user_update/<int:id>",views.user_update,name="user_update"),
    path("user_delete/<int:id>",views.user_delete,name="user_delete"),

    path("staff_admin",views.staff_admin,name="staff_admin"),
    path("staff_update/<int:id>",views.staff_update,name="staff_update"),
    path("staff_delete/<int:id>",views.staff_delete,name="staff_delete"),

    path("driver_admin",views.driver_admin,name="driver_admin"),
    path("driver_update/<int:id>",views.driver_update,name="driver_update"),
    path("driver_delete/<int:id>",views.driver_delete,name="driver_delete"),

    path("staff_index",views.staff_index,name="staff_index"),
    path("driver_index",views.driver_index,name="driver_index"),
]