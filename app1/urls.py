from django.urls import path

from app1 import admin
from app1.views import XYZ, testing1

urlpatterns = [
    path('xyz/', XYZ),
    path('test1/', testing1),
]