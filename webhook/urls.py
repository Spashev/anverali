from django.urls import path, include

from webhook.views import ContactViewSet, MockBackUrlViewSet


urlpatterns = [
    path('contacts/', ContactViewSet.as_view()),
    path('results/', MockBackUrlViewSet.as_view()),
]
