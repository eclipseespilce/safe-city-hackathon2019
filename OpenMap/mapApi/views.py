from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json
import logging


logger = logging.getLogger(__name__)


@csrf_exempt
def points_by_group(request, groupId):
    group_id = int(groupId)
    logger.debug("Send for group_id = {}".format(group_id))
    if request.method == 'GET':
        data = {
            "points":[
                {
                    "id": "1",
                    "latitude": 54.697929,
                    "longitude": 20.533874,
                    "status": "1",
                    "group": "1",
                    "category": "1",
                    "description": "Some description right here",
                    "photoUrl": "https://saffakfnla/img.png"
                },
                {
                    "id": "2",
                    "latitude": 51.697929,
                    "longitude": 22.533874,
                    "status": "3",
                    "group": "3",
                    "category": "4",
                    "description": "Some description right here",
                    "photoUrl": "https://saffakfnla/img.png"
                },
                ]
        }

        return HttpResponse(json.dumps(data))


@csrf_exempt
def groups_list(request):
    if request.method == 'GET':
        data = {
            "groups": [
                {
                    "id": "1",
                    "name": "Trashes"
                },
                {
                    "id": "2",
                    "name": "Toilets"
                },
                {
                    "id": "3",
                    "name": "Green things"
                },
            ]
        }

        return HttpResponse(json.dumps(data))


@csrf_exempt
def add_point(request):
    if request.method == 'POST':
        for key in request.POST:
            logger.debug("{}: {}".format(key, request.POST[key]))

        return HttpResponse("Received")
