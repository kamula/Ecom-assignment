from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from accounts.models import Account
from .models import Category, Product
from . serializers import CategorySerializer,ProductSerializer,GetProductSerializer


@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def create_category(request):
    # create category
    if request.method == 'POST':
        context = {}
        name = request.data.get('name').lower()
        data ={
            "name":name
        }
        serializer = CategorySerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            context['status'] = 'success'            
            context['message'] = 'successfully added new category'
            return Response(context,status=status.HTTP_201_CREATED)
        context['status'] = 'fail'
        context['message'] = serializer.errors
        return Response(context,status=status.HTTP_400_BAD_REQUEST)

    #GET all categories 
    if request.method == 'GET':
        context = {}
        if not request.user.is_superuser:
            context['status'] = 'fail'
            context['message'] = 'unauthorized access'
            return Response(context,status=status.HTTP_401_UNAUTHORIZED)
        categories = Category.objects.all()
        serializer = CategorySerializer(categories,many = True)
        context['status'] = 'success'
        context['data'] = serializer.data
        return Response(context,status=status.HTTP_200_OK)

# class Product()
@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def product_view(request):
    context = {}
    if request.method == "POST":
        data = request.data
        data._mutable = True 
        data['created_by'] = request.user.id
        serializer = ProductSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            context['status'] = "success"
            context['message'] = "product added"            
            return Response(context,status=status.HTTP_201_CREATED)
        context['status'] = "fail"
        context['message'] = serializer.errors
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    # get request
    if request.method == "GET":
        products = Product.objects.all()
        if products:

            serializer = GetProductSerializer(products,many = True)
            
            context['status'] = 'success'
            context['data'] = serializer.data
            return Response(context,status=status.HTTP_200_OK) 
        context['status'] = 'fail'
        context['message'] = 'no products'
        return Response(context,status=status.HTTP_404_NOT_FOUND) 

