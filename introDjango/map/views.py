from django.http import JsonResponse


# Create your views here.

def get_dict(request):
    data = {
        "x": 1,
        "y": 2,
        "z": 3
    }
    response = JsonResponse(data)
    return response