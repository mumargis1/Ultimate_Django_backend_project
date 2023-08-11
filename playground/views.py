from django.shortcuts import render
<<<<<<< HEAD
# from django.core.cache import cache
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
import logging
import requests


logger = logging.getLogger(__name__)

class HOME_VIEW(APIView):

    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin  is offline')
        return render(request, 'hello.html', {'name': 'data'})

=======
from django.http import HttpResponse


# Create your views here.
def say_hello(request):
    x=1
    return render(request, 'hello.html', {'name': 'umar'})
>>>>>>> a77aecced6d01cf351118df2ea482b17fbe03da9
