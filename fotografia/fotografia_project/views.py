from django.views.generic import TemplateView

class IndexPage(TemplateView):
    template_name = "index.html"

class ApiPage(TemplateView):
    template_name = "apiIndex.html"
