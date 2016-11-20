from django.shortcuts import render
from rasp_do_you_feel_lucky_punk_services import do_you_feel_lucky_punk

def is_ps3_online(request):
    result = do_you_feel_lucky_punk.check_is_ps3_on_network()
    return render(request, 'base.html', {'result': result})
