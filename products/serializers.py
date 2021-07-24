from accounts.models import Account
from django.db.models import fields
from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']


class ProductSerializer(serializers.ModelSerializer):
    # created_by = serializers.RelatedField(source = Account,read_only=True)
    # created_by = serializers.PrimaryKeyRelatedField(many=True,read_only=True,pk_field=serializers.UUIDField(format='hex'))
    # created_by = serializers.SerializerMethodField('get_created_by_name',read_only=True)
    # category = serializers.SerializerMethodField('get_category_name',read_only=True)
    class Meta:
        model = Product
        fields = ['id','name','price','created_by','category']   

    def get_created_by_name(self,obj):
        return f'{obj.created_by.email}'

    def get_category_name(self,obj):
        return obj.category.name

class GetProductSerializer(serializers.ModelSerializer):
    # created_by = serializers.RelatedField(source = Account,read_only=True)
    # created_by = serializers.PrimaryKeyRelatedField(many=True,read_only=True,pk_field=serializers.UUIDField(format='hex'))
    created_by = serializers.SerializerMethodField('get_created_by_name',read_only=True)
    category = serializers.SerializerMethodField('get_category_name',read_only=True)
    class Meta:
        model = Product
        fields = ['id','name','price','created_by','category']   

    def get_created_by_name(self,obj):
        return f'{obj.created_by.email}'

    def get_category_name(self,obj):
        return obj.category.name
