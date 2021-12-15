from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password','address','personal_mobile_no','date_of_birth','gender','guardain_name']
        extra_kwargs = {
            'created':{'read_only':True},
            'last_modified':{'read_only':True},
            'password':{'write_only':True}
        }
