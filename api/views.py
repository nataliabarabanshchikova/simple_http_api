from rest_framework.viewsets import ModelViewSet

from notes.serializers import NoteSerializer


class NoteAPIViewSet(ModelViewSet):
    permission_classes = ()
    serializer_class = NoteSerializer
    queryset = serializer_class.Meta.model.objects.all().order_by('date_create')
    lookup_field = 'id'
    lookup_url_kwarg = 'note_id'
