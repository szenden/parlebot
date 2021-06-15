from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('kamerstukken/', views.kamerstukken, name='kamerstukken'),
    path('kamerstukken_minister/', views.kamerstukken_minister, name='kamerstukken_minister'),
    path('kamervragen_beantwoorden/', views.kamervragen_beantwoorden, name='kamervragen_beantwoorden'),
    path('kamervragen_antwoorden_bekijken/', views.kamervragen_antwoorden_bekijken, name='kamervragen_antwoorden_bekijken'),
    path('questions/', views.questions, name='questions'),
    path('parlementarier_portaal/', views.parlementarier_portaal, name='parlementarier_portaal'),
    path('minister_portaal/', views.minister_portaal, name='minister_portaal'),
    path('login/', views.login, name='login'),
    path('wachtwoord_vergeten/', views.wachtwoord_vergeten, name='wachtwoord_vergeten'),
    path('wachtwoord_reset/', views.wachtwoord_reset, name='wachtwoord_reset'),
    path('parlementarier_kamervragen_stellen/', views.parlementarier_kamervragen_stellen, name='parlementarier_kamervragen_stellen'),
    path('parlementarier_kamervragen_bekijken/', views.parlementarier_kamervragen_bekijken, name='parlementarier_kamervragen_bekijken'),
    path('kamervragen_versturen/', views.kamervragen_versturen, name='kamervragen_versturen'),
    path('kamervragen_antwoorden_a/', views.kamervragen_antwoorden_a, name='kamervragen_antwoorden_a'),
    path('kamervragen_antwoorden_b/', views.kamervragen_antwoorden_b, name='kamervragen_antwoorden_b'),
    path('kamervragen_antwoorden_versturen/', views.kamervragen_antwoorden_versturen, name='kamervragen_antwoorden_versturen'),
    path('kamervragen_minister_antwoorden/', views.kamervragen_minister_antwoorden, name='kamervragen_minister_antwoorden'),



        #in the below section i am testing various database inserts, which will be deleted later on.
    path('dbconnect/', views.dbconnect, name='dbconnect'),
    path('testdbinput/', views.testdbinput, name='testdbinput'),

    path('insertform/', views.insertform, name='insertform'),
    path('form_test/', views.form_test, name='form_test'),
]
