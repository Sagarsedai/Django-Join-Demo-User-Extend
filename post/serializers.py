from rest_framework import serializers 
from .models import Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__' 
        extra_kwargs = {
            'id':{'read_only':True},
            'created':{'read_only':True},
            'last_modified':{'read_only':True}
        }

