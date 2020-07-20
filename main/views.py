import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from sliceme.solver import process


def index(request):
    data = dict()
    return render(request, "main.html", data)


def process_request(request):
    if request.is_ajax() and request.method == "POST":

        code = request.POST.get('code', None)

        response = process(code)
        response_data = {"response": str(response), "received": str(code)}
        return HttpResponse(json.dumps(response_data))
    else:
        return HttpResponse("BAD REQUEST!!! (GET)")
