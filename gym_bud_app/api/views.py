from django.http import JsonResponse
from gym_bud_app.models import Room
from rest_framework.decorators import api_view
from rest_framework.response import Response


def getRoutes(request):
    routes = [
        "GET /api",
        "GET /api/rooms",
        "GET /api/room/:id"
    ]

    return JsonResponse(routes, safe=False)

def getRooms(request):
    rooms = Room.objects.all()

    return 


