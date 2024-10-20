from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('steel-gates/', SteelGatesView.as_view(), name="steel-gates"),
    path('single-composite-gates/', SingleCompositeGatesView.as_view(), name="single-composite-gates"),
    path('double-composite-gates/', DoubleCompositeGatesView.as_view(), name="double-composite-gates"),
    path('railings/', RailingsView.as_view(), name="railings"),
    path('security/', SecurityView.as_view(), name="security"),
    path('powder-coating/', PowderCoatingView.as_view(), name="powder-coating"),
]
