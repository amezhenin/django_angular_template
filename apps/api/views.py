import json
from django.contrib import auth
from django.http import JsonResponse


def user_to_dict(user):
    return {
        "username": user.username,
        "email": user.email,
        "is_admin": user.is_superuser,
        "first_name": user.first_name,
        "last_name": user.last_name
    }


def login(request):
    """
    Login functionality for API
    """

    if request.method == 'GET':
        user = request.user
        if user.is_authenticated():
            return JsonResponse(user_to_dict(user))
        else:
            return JsonResponse({"message": "not authenticated"}, status=403)

    if request.method == 'POST':
        try:
            assert 'application/json' in request.META['CONTENT_TYPE']
            data = json.loads(request.body)
            assert 'username' in data
            assert 'password' in data
        except AssertionError:
            return JsonResponse({"message": "JSON request with username and password expected "}, status=400)

        user = auth.authenticate(username=data['username'],
                                 password=data['password'])
        if user is None:
            return JsonResponse({"message": "Wrong credentials"}, status=400)

        auth.login(request, user)
        return JsonResponse(user_to_dict(user))

    return JsonResponse({"message": "GET or POST method required"}, status=400)


def logout(request):
    auth.logout(request)
    return JsonResponse({"message": "success"})
