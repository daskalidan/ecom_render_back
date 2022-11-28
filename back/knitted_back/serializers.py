from django.contrib.auth.models import User
from .models import Category, Product
from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'description', 'category', 'name', 'price','image', 'get_thumbnail')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'cat_name')
        

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['is_staff'] = user.is_staff
        # ...

        return token


class RegisterSerializer(serializers.ModelSerializer):
    # address = serializers.CharField(max_length=100, blank=False, null=False, default='unknown')
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    class Meta:
        model = User
        # fields = ('username', 'password', 'email', 'is_staff', 'address')
        fields = ('__all__')

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            is_staff=validated_data['is_staff'],
        )
        # user.userProfile.address = validated_data['address']
        user.save()
        
        return user        