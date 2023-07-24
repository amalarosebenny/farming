from .import views
from django.urls import path
app_name='collegeapp'
urlpatterns = [
    path('',views.fun,name='fun'),
]