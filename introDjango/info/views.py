from django.http import JsonResponse


# Create your views here.

def info(request):
    response = JsonResponse({'foo': 'bar'})
    return response

def info_boo(request):
    response = JsonResponse({'boo': 'bar'})
    return response
