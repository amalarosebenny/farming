from django.urls import path
from accounts import views
app_name='accounts'
urlpatterns=[
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('page1',views.page1,name='page1'),
    path('r^create_view/',views.create_view,name='create_view'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),#AJAX
    path('msg/',views.msg,name='msg')
]