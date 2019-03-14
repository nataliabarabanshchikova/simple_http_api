from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    date_create = serializers.SerializerMethodField(read_only=True)
    date_update = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Note
        read_only_fields = ('id', 'date_create', 'date_update', )
        fields = read_only_fields + ('title', 'text')

    def get_date_create(self, instance):
        return int(instance.date_create.timestamp())

    def get_date_update(self, instance):
        return int(instance.date_update.timestamp())
