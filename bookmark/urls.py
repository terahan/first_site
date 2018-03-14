from django.urls import path
from .views import *

app_name = 'bookmark'

urlpatterns = [
    path('',BookmarkListView.as_view(),name="index"),
    path('add/',BookmarkCreateView.as_view(),name='create'),
    path('update/<int:pk>',BookmarkUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',BookmarkDeleteView.as_view(),name='delete'),
]
