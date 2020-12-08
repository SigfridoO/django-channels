from django.shortcuts import render

from django.views.generic import View
from braces.views import CsrfExemptMixin

from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.utils.decorators import method_decorator


from django.http import HttpResponse




from django.middleware.csrf import get_token


from chat import consumers
import json

class hookView (CsrfExemptMixin, View):
    
    
    def post(self, request, *args, **kwargs):


        consumers.receive("Mensaje")

        return HttpResponse('Resultado desde post')


    def get(self, request, *args, **kwargs):

        token = get_token(request)

        datos = {'mensaje': 'Resultado desde get', 'csrf_token': token}
        return HttpResponse(json.dumps( datos ))
