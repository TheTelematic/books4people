from django.conf import settings
from django.http import JsonResponse
from google.auth.transport import requests
from google.oauth2 import id_token


def login(request):
    template = 'accounts/login.html'
    extras_js = ['accounts/js/login.js', ]

    if request.is_ajax() and request.method == 'GET':
        print "REQUEST ACCEPTED"

        token_id = request.GET['id_token']

        try:
            idinfo = id_token.verify_oauth2_token(token_id, requests.Request(), settings.CLIENT_ID)

            if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')

            userid = idinfo['sub']

            return JsonResponse({'user_authenticated': True})
        except ValueError:
            # Invalid token
            return JsonResponse({'user_authenticated': False})

    return JsonResponse({})
