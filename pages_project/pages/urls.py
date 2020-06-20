from django.urls import path
from .views import HomePageView, AboutPageView, HistoryPageView, BasePageView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about',AboutPageView.as_view(), name='about'),
    path('history', HistoryPageView.as_view(), name='history'),
    path('base', BasePageView.as_view(), name='base'),
]
