from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view,name='login'),
    path('register/', views.register_view,name='register'),
    path('logout/', views.logout_view,name='logout'),
    path('home/', views.home,name='home'),
    path('create_class/',views.create_class, name='create_class'),
    path('join_class/',views.join_class,name='join_class'),
    path('class/<int:id>',views.render_class,name='render_class'),
    path('create_assignment/<int:classroom_id>',views.create_assignment,name='create_assignment'),
    path('assignment_summary/<int:assignment_id>',views.assignment_summary,name='assignment_summary')
]