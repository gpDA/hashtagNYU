from rest_framework import serializers
from main.models import Main, Tweet

class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = ('id', 'name', 'email', 'message')

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        exclude = []
