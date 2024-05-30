from django.urls import path
from . import views
urlpatterns = [
    path('add/',views.album, name='album'),
    path('edit/<int:id>', views.edit_album, name='edit_album'),
]


