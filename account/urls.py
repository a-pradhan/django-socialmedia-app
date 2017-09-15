from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #url(r'^register/$', views.register, name='register'),
    url(r'^login/$', auth_views.LoginView.as_view(),name="login"),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name="logout"),
    #url(r'^logout-then-login/$',auth_views.logout_then_login, name="logout_then_login"),

    #url(r'^password-change/$',auth_views.PasswordChangeView.as_view(), name="password_change"),
    #url(r'^password-change/done/$',auth_views.PasswordChangeDoneView.as_view(), name="password_change"),
    url(r'^$',views.dashboard,name="dashboard"),


]
