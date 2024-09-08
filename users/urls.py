from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', LogoutView.as_view(template_name='apptalentos/inicio.html'), name="Logout"),
    path('edit/', views.editar_perfil, name="EditarPerfil"),
    path('cambiar_pass/', views.CambiarContrasenia.as_view(), name="CambiarPass"),
    path('profile/', views.profile, name='Profile'),
]

