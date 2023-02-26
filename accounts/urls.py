from django.urls import path
from . import views
urlpatterns = [
    path('api/register/',views.RegisterView.as_view()),
    path('api/activate/',views.ActivateUser.as_view()),
    path('api/login/',views.Login.as_view(),name='login'),
    path('api/reset_password/',views.ResetPassword.as_view()),
    path('api/check_code/',views.CheckCode.as_view()),
    path('api/set_password/',views.SetPassword.as_view()),
    path('api/change_password/',views.ChangePassword.as_view()),
    #path('profil/',views.profil,name='profil'),
    #path('profil/edit',views.profil_edit,name='profil_edit'),
]