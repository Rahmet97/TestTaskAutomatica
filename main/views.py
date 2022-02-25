from django.db.models import Q
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ShoppingCenterSerializer, VisitSerializer
from .models import *


@api_view(['GET'])
def get_list(request):
    try:
        phone = request.GET.get('phone', '')
        shopping_center = ShoppingCenter.objects.filter(worker__phone__icontains=phone)
        shopping_center_list = ShoppingCenterSerializer(shopping_center, many=True)
        data = {
            'success': True,
            'data': shopping_center_list.data
        }
    except Exception as e:
        data = {
            'success': False,
            'message': f'{e}'
        }
        return Response(data, status=405)
    return Response(data, status=200)


@api_view(['POST'])
def visit(request):
    try:
        phone = request.POST.get('phone', '')
        shopping_center_id = request.POST.get('shopping_center_id', 0)
        latitude = request.POST.get('latitude', 0)
        longitude = request.POST.get('longitude', 0)

        if ShoppingCenter.objects.filter(Q(id=shopping_center_id) and Q(worker__phone=phone)).exists():
            new_visit = Visit.objects.create(shopping_center_id=shopping_center_id, latitude=latitude, longitude=longitude)
            new_visit.save()
            visits = VisitSerializer(new_visit)
            data = {
                'success': True,
                'data': visits.data
            }
        else:
            data = {
                'success': False,
                'message': 'Номер телефона не совпадает!!!'
            }
            return Response(data, status=401)
    except Exception as e:
        data = {
            'success': False,
            'error': f'{e}'
        }
        return Response(data, status=405)
    return Response(data, status=201)
