from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser, FormParser

import logging

from mapApi.models import Group, MapPoint
from mapApi.serializers import GroupSerializer, MapPointSerializer

logger = logging.getLogger(__name__)


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def points_by_group(request, groupId):
    map_points = MapPoint.objects.filter(group__pk=groupId).all()
    serializer = MapPointSerializer(map_points, many=True)
    data = {"points": serializer.data}
    return Response(data)


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def groups_list(request):
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True)
    data = {'groups': serializer.data}
    return Response(data)


@api_view(['POST'])
@renderer_classes((JSONRenderer, FormParser))
def add_point(request):
    data = JSONParser().parse(request)
    serializer = MapPointSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
