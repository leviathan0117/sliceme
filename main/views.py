import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

def index(request):
    data = dict()
    return render(request, "main.html", data)

def process_request(request):
    if request.is_ajax() and request.method == "POST":
        object_id = request.POST.get('id', None)
        value = request.POST.get('value', None)
        data = {"Received from id: ": str(object_id), "Data: ": str(value), "Response: ": "kek"}
        return HttpResponse(json.dumps(data))
    else:
        object_id = request.GET.get('id', None)
        value = request.GET.get('value', None)
        return HttpResponse("BAD REQUEST!!! (GET)\n\n" +
                            "But I still can answer it though: Received from id: " +
                            str(object_id) + " Data: " + str(value) + " Response: kek" +
                            "\n\nAnd the answer is not json-style, 'cause you're a moron, who uses GET, not POST")
