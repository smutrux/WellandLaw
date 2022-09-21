from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-us/', views.aboutus, name="about-us"),
    path('career-centre/', views.careercentre, name="career-centre"),
    path('contact-us/', views.contactus, name="contact-us"),
    path('cpd-events/', views.cpdevents, name="cpd-events"),
    path('events-details/<str:pk>/', views.eventsdetails, name="events-details"),
    path('', views.index, name="index"),
    path('landing-page/', views.landingpage, name="landing-page"),
    path('library/', views.library, name="library"),
    path('membership-page/', views.membershippage, name="membership-page"),
    path('practice-portals/', views.practiceportals, name="practice-portals"),
    path('public-resourcess/', views.publicresources, name="public-resources"),

]
