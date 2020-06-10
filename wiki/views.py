from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    # DeleteView,
)
from .models import Content
from django.urls import reverse
from django.db.models import Q
from .forms import ContentModelForm


def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if q:
        contents = Content.objects.filter(Q(title__icontains=q))
        if contents:
            context = {'query': q, 'contents': contents}
            template = 'wiki/results.html'
            print("Search found query from the database")
            return render(request, template, context)
        else:
            context = {'query': q}
            template = 'wiki/results.html'
            print("Search didn't match with any query in the database")
            return render(request, template, context)
    else:
        context = {}
        template = 'wiki/results.html'
    return render(request, template, context)


def home(request):
    context = {
        'contents': Content.objects.all()
    }

    return render(request, 'wiki/home.html', context)


class WikiResultsView(ListView):
    model = Content
    template_name = 'wiki/results.html'


class WikiListView(ListView):
    model = Content
    template_name = 'wiki/home.html'
    ordering = ['-date_posted']


class WikiDetailView(DetailView):
    model = Content


class WikiCreateView(CreateView):
    model = Content
    template_name = 'wiki/content_form.html'
    queryset = Content.objects.all()
    form_class = ContentModelForm

    def get_success_url(self):
        return reverse("wiki-details", kwargs={"pk": self.object.id})


class WikiUpdateView(UpdateView):
    model = Content
    form_class = ContentModelForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("wiki-details", kwargs={"pk": self.object.id})


# class WikiDeleteView(DeleteView):
#     model = Content
#
#     def get_success_url(self):
#         return reverse("wiki-home")


class WikiEditsView(DetailView):
    model = Content
    template_name = 'wiki/edits.html'

    def get_success_url(self):
        return reverse("wiki-details", kwargs={"pk": self.object.id})
