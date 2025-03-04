from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        # Safely handle the case where self.user may be None or have no groups
        if self.user and self.user.groups.exists():
            data['role'] = self.user.groups.first().name
        else:
            data['role'] = None
        
        return data