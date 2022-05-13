from django.urls import path
from django.views.generic import TemplateView
from .views import EmployeeRegisterView

urlpatterns = [
    path("", TemplateView.as_view(template_name = "user/index.html")),
    path("dashboard", TemplateView.as_view(template_name = "user/dashBoard.html"), name="dashboard"),
    path("register_employee",EmployeeRegisterView.as_view(), name="register_employee"),   
]