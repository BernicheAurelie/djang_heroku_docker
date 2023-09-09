from django.http import JsonResponse


def ping(request):
    data = {'ping': 'pong!'}
    return JsonResponse(data)

def titi(request):
    data = {'titi': 'tata!'}
    return JsonResponse(data)