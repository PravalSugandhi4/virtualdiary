from django.urls import path
from mytodo import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.loginpage,name='login'),
    path('register/',views.registerpage,name='register'),
    path('home/',views.homepage,name='homepage'),
    path('logout/',views.logoutpage,name='logout'),
    
  
]
