from rest_framework import serializers
from .models import Group, Category
from django.contrib.auth.models import User
class CategorySerializer(serializers.ModelSerializer):

    group = serializers.SlugRelatedField(many=True, queryset=Group.objects.all(), slug_field='title')
    class Meta:
        model = Category
        fields = (
                'id',
                'name',
                'group',
                )     

class GroupSerializer(serializers.ModelSerializer):
    
    # category = serializers.SlugRelatedField(many=True, queryset=Category.objects.all(), slug_field='name')
    user = serializers.SlugRelatedField(many=True, queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Group
        fields = (
                'id',
                'user',
                'title',
                'description',   
                # 'category',
                )


