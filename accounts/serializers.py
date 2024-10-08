from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth import get_user_model

###############################

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True,
            validators = [UniqueValidator(queryset=User.objects.all())])
    password_1 = serializers.CharField(required=True,write_only = True)
    password_2 = serializers.CharField(required=True,write_only = True)
    
    class Meta:
        model = User
        
        fields = (
            'email','username','password_1','password_2','first_name','last_name',
        )
        
        extra_kwargs ={
            'first_name':{'required':False},
            'last_name':{'required':False},
        }
    
    def validate(self, attrs):
        if attrs['password_1'] != attrs['password_2']:
            raise serializers.ValidationError({
                'password':'Password is didn match !'
            })
        return super(RegisterSerializer,self).validate(attrs)    
    def create(self,validate_data):
        user = User.objects.create_user(
            username = validate_data['username'],
            email = validate_data['email'],
            first_name =  validate_data.get('first_name',''),  
            last_name =  validate_data.get('last_name',''),  
            password = validate_data['password_1'],
             
        )
        # user.set_password(validate_data['passsword_1'])
        # user.save()
        return user