from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import Counter


@api_view(['POST'])
def lambda_function(request):
    data = request.data.get('question')
    lista = list(Counter(data).elements())
    lista_final = sorted(lista, key=lista.count, reverse=True)

    return Response({'solution': lista_final})
