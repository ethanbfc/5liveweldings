from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'

class SteelGatesView(TemplateView):
    template_name = 'steel_gates.html'

class SingleCompositeGatesView(TemplateView):
    template_name = 'single_composite_gates.html'

class DoubleCompositeGatesView(TemplateView):
    template_name = 'double_composite_gates.html'

class RailingsView(TemplateView):
    template_name = 'railings.html'

class SecurityView(TemplateView):
    template_name = 'security.html'

class PowderCoatingView(TemplateView):
    template_name = 'powder_coating.html'
