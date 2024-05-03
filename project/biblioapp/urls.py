from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('biblio/', views.biblio, name='biblio'),
    path('change_password/', views.change_password, name='change_password'),
    path('admin/', admin.site.urls),
    #path('success/', views.success, name='success'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
