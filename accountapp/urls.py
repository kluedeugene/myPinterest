from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountapp"

urlpatterns = [

    path('login/', LoginView.as_view(template_name= 'accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),   # 특정 유저의 키(primary key)가 필요하다.
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),  # 특정 유저의 키(primary key)가 필요하다.
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),  # 특정 유저의 키(primary key)가 필요하다.

]
