# drinks/views.py
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    # Handle GET and POST requests for the Drink model.
    
    if request.method == 'GET':
        # Get all drinks, serialize them, and return JSON.
        #get all the drinks
        drinks = Drink.objects.all()
        #serialize them
        serializer = DrinkSerializer(drinks, many=True)
        #return json
        # return JsonResponse({'Drink': serializer.data}, safe=False)
        return Response(serializer.data)
    
    if request.method == 'POST':
        # Create a new drink based on POST data.
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):
    # Handle GET, PUT, and DELETE requests for a specific drink.
    # drink = get_object_or_404(Drink, pk=id)
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        # Serialize and return details of a specific drink.
        serializer = DrinkSerializer(drink) 
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        # Update the details of a specific drink based on PUT data.
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        # Delete a specific drink.
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    