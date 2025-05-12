from django.shortcuts import render

# Create your views here.
class AboutList(generic.ListView):
    queryset = About.objects.first()
    template_name = "about/index.html"
