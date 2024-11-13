from rest_framework import serializers
from .models import CustomUser, Organization




class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = "__all__"

    
class UserRegistrationSerializer(serializers.ModelSerializer):
    role = serializers.CharField(default='general')
    password = serializers.CharField(write_only=True)  # Ensure password is write-only

    class Meta:
        model = CustomUser
        fields = "__all__"

    def create(self, validated_data):
        # Remove the password from the validated data
        password = validated_data.pop('password')
        
        # Create the user without the password initially
        user = CustomUser(**validated_data)
        
        # Hash the password using set_password
        user.set_password(password)
        
        # Save the user instance
        user.save()
        
        return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
