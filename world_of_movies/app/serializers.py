from rest_framework import serializers

class MovieSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    cover = serializers.URLField()
    title = serializers.CharField()
    director = serializers.CharField()
    year = serializers.IntegerField()
    genre = serializers.CharField()
    rating = serializers.FloatField()