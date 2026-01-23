from django.urls import path
from .views import TodoListDetailedAPIs
from .views import TodoListBriefAPIs

urlpatterns = [
    # Converting the class based view in a callable view function. New instance of view is created per request by DRF
    # Defined endpoints and connected them to related view classes
    # Endpoint for all todos (GET and POST), handled by TodoListDetailedAPIs class
    path('todos/', TodoListDetailedAPIs.as_view()),

    # Endpoint for a single todo (PUT and DELETE) identified by id, handled by TodoListBriefAPIs class
    path('todos/<int:id>/', TodoListBriefAPIs.as_view())
]
