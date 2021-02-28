from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

app_name = 'api'
urlpatterns = [
    path('user/', include('apps.users.urls')),
]
