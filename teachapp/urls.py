from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

	path('populate', views.populate, name='populate'),
	path('home', views.home, name='home'),
    path('list', views.teachers_list, name='teachers-list'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('export/csv-database/', views.csv_database_write, name='csv_database_write'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup', views.signup, name='signup'),

]
