from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sites.shortcuts import get_current_site

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import JSONParser, FormParser, FileUploadParser, MultiPartParser

import logging
import random
import string

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
def all_points(request):
    map_points = MapPoint.objects.all()
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



def get_request_root_url(request):
    scheme = 'https' if request.is_secure() else 'http'
    site = get_current_site(request)
    return '%s://%s' % (scheme, site)


@api_view(['POST'])
def upload_image(request):
    filename = ''.join([random.choice(string.ascii_lowercase) for i in range(30)])
    filepath = '{}{}.jpeg'.format('media/', filename)
    with open(filepath,'wb+') as destination:
        for key, value in request.POST.items():
            #destination.write(bytes(key, 'utf-8'))
            destination.write(key)

    url = '{}/{}'.format(get_request_root_url(request), filepath)
    return Response({'url': url},status=201)


class FileUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def put(self,request, format = None):
        file_obj = request.FILES['file']
        file_obj.seek(0)
        data = file_obj.read()

        filename = ''.join([random.choice(string.ascii_lowercase) for i in range(30)])
        filepath = '{}{}.jpeg'.format('media/', filename)
        with open(filepath,'wb+') as destination:
            destination.write(data)

        url = '{}/{}'.format(get_request_root_url(request), filepath)
        return Response({'url': url},status=201)

