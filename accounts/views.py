from django.contrib.auth import authenticate
from .utils import validate_email,get_tokens_for_user
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Account
from .serializers import RegistrationSerializer

@api_view(['GET'])
def get_urls(request):
    data =[
        'POST:{{url}}/api/v1/users/signup',
        'POST:{{url}}/api/v1/users/login',
        'GET & POST product categories :{{url}}api/v1/products/categories',
        'GET & POST products :{{url}}api/v1/products/',
    ]
    return Response(data,status=status.HTTP_200_OK)

@api_view(['POST'])
def signup_view(request):
    '''user registration'''
    if request.method == 'POST':
        context = {}
        # data = request.data
        email = request.data.get('email')
        if validate_email(email) != None:
            context['status'] = 'fail'
            context['message'] = 'email already in use'
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
                    
        serializer = RegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            context['status'] = 'success'
            context['message'] = 'successssfully registered'
            return Response(context,status=status.HTTP_201_CREATED)
        context['status'] = 'fail'
        context['message'] = serializer.errors
        return Response(context,status=status.HTTP_400_BAD_REQUEST)

        
   
@api_view(['POST'])
def login_view(request):
    '''user login'''
    if request.method == 'POST':
        context = {}
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            context['status'] = 'fail'
            context['message'] = 'please provide credentials'
            return Response(context,status=status.HTTP_400_BAD_REQUEST)
        account = authenticate(email=email,password=password)
        if account:
            token = get_tokens_for_user(account)
            context['status'] = 'success'
            context['token'] = token
            return Response(context,status=status.HTTP_200_OK)
        context['status']= 'success'
        context['message']= 'Invalid credentials'
        return Response(context,status=status.HTTP_400_BAD_REQUEST)

def logout_view(request):
    '''user logout'''
    return
