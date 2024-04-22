from rest_framework import serializers


class ContactSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class QuerySerializer(serializers.Serializer):
    contacts = ContactSerializer(many=True)
    back_url = serializers.URLField()
