from rasp_do_you_feel_lucky_punk_services import do_you_feel_lucky_punk
from django.http import JsonResponse


def is_ps3_online(request):
    result = do_you_feel_lucky_punk.check_is_ps3_on_network()
    return JsonResponse({'result': result})

def is_server(request):
    return JsonResponse({'result': "True"})