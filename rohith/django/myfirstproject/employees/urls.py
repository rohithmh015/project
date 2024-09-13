from django.urls import path
from.import views

urlpatterns = [
    path('create/',views.create_employee,name="create_employee"),
    path('read/', views.read_employees, name='read_employees'),
    path('update/<str:employee_name>/', views.update_employee_department, name='update_employee_department'),
    path('delete/<str:employee_name>/', views.delete_employee, name='delete_employee'),
    path('filter/', views.filter_employees_by_department, name='filter_employees_by_department'),
    path('average_salary/', views.average_salary, name='average_salary'),
    path('high_paid/', views.high_paid_employees, name='high_paid_employees'),
]
