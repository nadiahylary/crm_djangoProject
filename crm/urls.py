from django.urls import path

from crm import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('customers', views.customers_List, name='customers'),
    path('customers/edit<int:pk>', views.edit_customer, name='edit'),
    path('customers/delete<int:pk>', views.delete_customer, name='delete')
]
