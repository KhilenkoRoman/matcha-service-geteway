from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token
from .views import GenericLeasesView

app_name = 'users'
urlpatterns = [
    path('token/', obtain_jwt_token, name='token_obtain_pair'),
    path('test/',
         GenericLeasesView.as_view(),
         name='asd'),

]
