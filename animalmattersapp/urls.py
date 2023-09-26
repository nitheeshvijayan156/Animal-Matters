from django import views
from django.urls import path
from . import views
 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('signup/',views.signup,name='signup'),
    path('',views.home,name='home'),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('donation/',views.donation,name="donation"),
    path('report/',views.report,name="report"),
     path('aboutus/',views.aboutus,name="aboutus"),
     path('logaboutus/',views.logaboutus,name="logaboutus"),
      

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)