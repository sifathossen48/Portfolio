from django.shortcuts import render
from django.views.generic import TemplateView

from website.models import Info, About, Client, Project, Experience, Education, Skill, Testimonial, Copyright


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = Info.objects.last()
        context['abouts'] = About.objects.last()
        context['clients'] = Client.objects.all()
        context['projects'] = Project.objects.all()
        context['experiences'] = Experience.objects.all()
        context['education'] = Education.objects.all()
        context['skill'] = Skill.objects.all()
        context['testimonials'] = Testimonial.objects.all()
        context['copyright'] = Copyright.objects.last()
        return context

