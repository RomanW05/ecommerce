from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from rest_framework import  serializers


from .models import User

User = get_user_model()



class ResisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password',)
        extra_kwargs = {
            'password':{'write_only': True},
        }
    
    def validate_data(self):
        data = self.get_initial()
        email = data.get('email')
        email_stored = User.objects.filter(email=email)
        if email_stored.exists():
            raise ValidationError("Email already registered")
        else:
            return data
    
    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'], password=validated_data['password'])
        return user
    

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')