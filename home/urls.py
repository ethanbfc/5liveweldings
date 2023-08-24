from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('steel-gates/', SteelGatesView.as_view(), name="steel-gates"),
    path('composite-gates/', CompositeGatesView.as_view(), name="composite-gates"),
    path('railings/', RailingsView.as_view(), name="railings"),
    path('security/', SecurityView.as_view(), name="security"),
    path('steel-framed-treated-timber-infill/', SteelFramedTreatedTimberInfillView.as_view(), name="steel-framed-treated-timber-infill"),
]