from django.urls import path
from . import views
from app.views import PetRegister, PetUpdate, PetDelete

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('userlogout/', views.userlogout, name='userlogout'),
    path('petdetails/<int:petid>/', views.petdetails, name='petdetails'),
    path("PetRegister/", PetRegister.as_view(), name="PetRegister"),
    path("PetUpdate/<int:pk>/", PetUpdate.as_view(), name="PetUpdate"),
    path("PetDelete/<int:pk>/", PetDelete.as_view(), name="PetDelete"),
    path("searchpets/", views.searchpets, name="searchpets"),
    path("searchbygender/", views.searchbygender, name="searchbygender"),
    path("req_password/", views.req_password, name="req_password"),
    path("reset_password/<uemail>", views.reset_password, name="reset_password")
    ]
