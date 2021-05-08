from django.urls import path
from .views import *


urlpatterns = [
    path("userEndPoint", userView),
    path("userSearchId/<int:id>" ,userDetailView),
    path("userSearchEmail/<str:email>", userSearch)
]
