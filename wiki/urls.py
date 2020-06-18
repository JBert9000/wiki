from django.urls import path
from .views import (
    WikiDetailView,
    WikiCreateView,
    WikiUpdateView,
    # WikiDeleteView,
    WikiEditsView,
    WikiResultsView,
    dummy_view,
    dummy_list_view,
)
from . import views


urlpatterns = [
    path('', views.home, name="wiki-home"),
    path('s/', views.search, name="wiki-search"),
    path('results/', WikiResultsView.as_view(), name="wiki-results"),
    path('content/new/', WikiCreateView.as_view(), name="wiki-create"),
    path('content/<int:pk>/update/', WikiUpdateView.as_view(), name="wiki-update"),
    # path('content/<int:pk>/delete/', WikiDeleteView.as_view(), name="wiki-delete"),
    path('content/<int:pk>/', WikiDetailView.as_view(), name="wiki-details"),
    path('content/<int:pk>/edits/', WikiEditsView.as_view(), name="wiki-edits"),
    path('dummy/', views.dummy_list_view, name="dummy-list"),
    path('dummy/<int:id>/', views.dummy_view, name="dummy-data"),
    path('dummy/<int:id>/edits/', views.dummy_edit_history, name="dummy-edits"),
]
