from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import router_details
from rest_framework.decorators import api_view, permission_classes
import datetime
import json
from .serializers import RouterSerializer
import logging

# Create your views here.

logging.basicConfig(filename="router.log", format='%(asctime)s %(message)s', filemode='w')
logger=logging.getLogger()

def index(request):
    return JsonResponse({'info': 'testing API', 'developer': 'neha'})


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def InsertRouterDetails(request):
    data = request.data
    # print(data)
    router_obj = router_details.objects.create(sapid=data['sapid'], hostname=data['hostname'], loopback=data['loopback'], macaddress=data['macaddress'])
    logger.info(f"router object with sapid {data['sapid']} created successfully at {datetime.datetime.now()}")
    return Response({'message': 'Successfully created router details', 'status_code': 201})


@api_view(['PATCH'])
def UpdateRouterDetails(request):
    data = request.data
    loopback = request.data.get('loopback')
    if not loopback:
        return Response({'message': 'Please provide loopback', 'status_code': 400}, status=status.HTTP_400_BAD_REQUEST)
    try:
        router_obj = router_details.objects.get(loopback=loopback, is_delete=False)
    except router_details.DoesNotExist:
        return Response({'message': 'Router of the respective loop back does not exist', 'status_code': 400},
                        status=status.HTTP_400_BAD_REQUEST)
    router_serializer = RouterSerializer(router_obj, data=data, partial=True)
    router_serializer.is_valid(raise_exception=True)
    router_serializer.save()
    logger.info(f"router object with loopback {loopback} updated successfully at {datetime.datetime.now()}")
    return Response({'message': 'Successfully updated router details', 'status_code': 201}, status=status.HTTP_201_CREATED)


def convert_ipv4(ip):
    return tuple(int(n) for n in ip.split('.'))
def check_ipv4_in(addr, start, end):
    return convert_ipv4(start) <= convert_ipv4(addr) <= convert_ipv4(end)

@api_view(['POST'])
def retrieveRouterDetailsbyIPrange(request):
    data=request.data
    startrange = request.data.get('start_range')
    endrange = request.data.get('end_range')

    if (not startrange) or (not endrange):
        return Response({'message': 'Please provide range', 'status_code': 400}, status=status.HTTP_400_BAD_REQUEST)

    router_obj = router_details.objects.filter(is_delete=False).values()

    #print(router_obj)
    for r_IP in router_obj:
        ip=r_IP['loopback']

        if not check_ipv4_in(ip, startrange, endrange):
            router_obj=router_obj.exclude(loopback=ip)
    serializer = RouterSerializer(router_obj, many=True)
    logger.info(f"router details with range fetched successfully at {datetime.datetime.now()}")
    return Response({'message': 'Successfully fetched router details', 'status_code': 200, 'data' : serializer.data}, status=status.HTTP_200_OK)


@api_view(['GET'])
def retrieveRouterDetails(request):
    router_details_values = router_details.objects.filter(is_delete=False).values()
    serializer = RouterSerializer(router_details_values , many=True)
    logger.info(f"router details fetched successfully at {datetime.datetime.now()}")
    return Response(
        {'message': 'Successfully fetched router details', 'status_code': 200, 'data': serializer.data},
        status=status.HTTP_200_OK)


@api_view(['DELETE'])
def DeleteRouterDetails(request):
    data = request.data
    loopback = request.data.get('loopback')
    if not loopback:
        return Response({'message': 'Please provide loopback', 'status_code': 400}, status=status.HTTP_400_BAD_REQUEST)
    try:
        router_obj = router_details.objects.get(loopback=loopback)
    except router_details.DoesNotExist:
        return Response({'message': 'Router of the respective loop back does not exist', 'status_code': 400},
                        status=status.HTTP_400_BAD_REQUEST)
    router_obj.is_delete = True
    router_obj.save()
    logger.info(f"router object with loopback {loopback} deleted successfully at {datetime.datetime.now()}")
    return Response({'message': 'Successfully deleted router details', 'status_code': 200}, status=status.HTTP_200_OK)
