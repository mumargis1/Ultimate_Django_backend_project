from django.urls import path
from . import views

<<<<<<< HEAD
# URLConf
urlpatterns = [
    path('hello/', views.HOME_VIEW.as_view())
]
=======

# URLConf
urlpatterns = [
    path('hello/', views.say_hello)

]
>>>>>>> a77aecced6d01cf351118df2ea482b17fbe03da9
