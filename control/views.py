from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import util

@csrf_exempt
def twitter_status(request):
    if request.method == "GET":
        return HttpResponse(status=400)
    username = request.POST['username']
    status = util.twitter_status()
    if status is None:
    	return HttpResponse(status=204)
    response_data = {'error': "none", 'status': status}
    return HttpResponse(json.dumps(response_data), content_type="application/json")

