from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('tracker/',views.tracker),
    path('about/',views.about),
    path('index/',views.index),
    path('contact/',views.contact),
]
