from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.HOME_VIEW.as_view())
]
