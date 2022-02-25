from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import get_list, visit

urlpatterns = [
    path('get-shopping-centers-list', get_list),
    path('visit', csrf_exempt(visit))
]
