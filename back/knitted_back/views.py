from decimal import Decimal
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import UpdateAPIView

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from django.contrib.auth import logout
from .models import Category, Order, OrderItem, Product
from .serializers import CategorySerializer, MyTokenObtainPairSerializer, ProductSerializer, RegisterSerializer

# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer  

@api_view(['POST'])
def register_my_user(request):
    print(request.data)
    new_user_serializer = RegisterSerializer(data=request.data)
    if new_user_serializer.is_valid():
        new_user = new_user_serializer.create(new_user_serializer.validated_data)
        new_user.userprofile.address = request.data['address']
        new_user.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(new_user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def log_out(request):
    logout(request)
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def all_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def all_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)    


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_new_category(request):
    print(request.user)
    if request.user.is_staff == True:
        new_category_serializer = CategorySerializer(data=request.data)
        print(request.data)
        if new_category_serializer.is_valid():
            new_category_serializer.save()
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(new_category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


class Create_new_product(APIView):
    permission_classes = [IsAuthenticated]
    parser_class = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        print(request.user)
        print(request.data)
        if request.user.is_staff == True:
            new_product_serializer = ProductSerializer(data=request.data)
            if new_product_serializer.is_valid():  
                new_product_serializer.save()
                products = Product.objects.all()
                serializer = ProductSerializer(products, many=True)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print('error', new_product_serializer.errors)
                return Response(new_product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class edit_product(UpdateAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        if request.user.is_staff == True:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            if serializer.is_valid():
                self.perform_update(serializer)
                products = Product.objects.all()
                all_serializer = ProductSerializer(products, many=True)
                return Response(all_serializer.data, status=status.HTTP_200_OK)
            else:
                print('error', serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)                   
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_product(request):
    try:
        product = Product.objects.get(pk=request.data['id'])
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.user.is_staff == True:
        product.delete()
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)    

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_category(request):
    print(request.data)
    try:
        category = Category.objects.get(pk=request.data['id'])
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.user.is_staff == True:
        category.delete()
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)         


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def place_an_order(request):
    client_order = request.data
    new_order = Order.objects.create(user=request.user,total_payment=Decimal(client_order['total_price']).quantize(Decimal('0.01')))

    for item in client_order['items']:
        product = Product.objects.get(id=item['id'])
        OrderItem.objects.create(order=new_order,item=product,quantity=item['quantity'])

    return Response(status=status.HTTP_201_CREATED)