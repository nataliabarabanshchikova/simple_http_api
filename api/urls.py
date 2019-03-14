from django.urls import re_path

from api.views import NoteAPIViewSet


note_list = NoteAPIViewSet.as_view(actions={
    'get': 'list',
    'post': 'create',
})
note_detail = NoteAPIViewSet.as_view(actions={
    'get': 'retrieve',
    'put': 'update',
})

urlpatterns = [
    re_path(r'^notes/$', note_list, name='note-list'),
    re_path(r'^notes/(?P<note_id>[0-9a-f-]+)/$', note_detail,
            name='note-detail'),
]
