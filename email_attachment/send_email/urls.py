# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns in your app
    path('email-attachment/', views.my_email_with_attachment_view, name='email-template'),
]