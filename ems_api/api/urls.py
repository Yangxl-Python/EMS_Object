from django.urls import path

from api import views

urlpatterns = [
    path('register/', views.UserRegisterAPIView.as_view()),
    path('login/', views.UserLoginViewSet.as_view({'post': 'login'})),

    path('emp/', views.EmployeeAPIView.as_view()),
    path('emp/<id>/', views.EmployeeAPIView.as_view()),

    path('get_time/', views.get_time)
]
