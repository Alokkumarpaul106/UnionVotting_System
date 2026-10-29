from .models import Candidate,Vote,EligibleVoter
from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email=serializers.CharField()
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

        

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            is_active=False
        )
        return user


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Candidate
        fields='__all__'

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vote
        fields='__all__'

class EligibleVoterSerializer(serializers.ModelSerializer):
    class Meta:
        model=EligibleVoter
        fields='__all__'