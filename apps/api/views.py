from django.http import HttpResponse, JsonResponse

# Create your views here.

def home(req):
    return JsonResponse({
        "message": "Hello",
        "data": list(range(5))
    })


