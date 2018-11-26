from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import Show, Actor


class ShowSerializer(serializers.ModelSerializer):
    actors = serializers.SlugRelatedField(many=True, queryset=Actor.objects.all(), slug_field='first_name')

    class Meta:
        model = Show
        fields = ('title', 'id', 'description', 'year', 'season_num', 'actors')

        def update(self, instance, validated_data):
            instance.title = validated_data.get("title", instance.title)
            instance.artist = validated_data.get("artist", instance.artist)
            instance.save()
            return instance


class ActorSerializer(serializers.ModelSerializer):
    shows = serializers.SlugRelatedField(many=True, queryset=Show.objects.all(), slug_field='title')

    class Meta:
        model = Actor
        fields = ('first_name', 'last_name', 'shows')

