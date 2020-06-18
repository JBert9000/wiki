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


dummy_data = {
    1: {
        'id': 1,
        'title': 'Fox',
        'content': 'This is dummy data that is not editable in this demo, but anyone is encouraged to create wiki posts which can also be edited by anyone. Typically a user can create, edit, and delete posts without making a profile. Links via the sidebar will automaically be made based on the title of each wiki post. Go back to the home page to check out more posts.',
        'date_posted': 'June 15th 2020',
        'date_updated': 'June 16th 2020',
        'history': {'June 15th 2020', 'June 16th 2020'},
    },
    2: {
        'id': 2,
        'title': 'Frog',
        'content': 'This is a picture of a frog.',
        'date_posted': 'June 15th 2020',
        'date_updated': 'June 16th 2020',
        'history': {'June 15th 2020', 'June 16th 2020'},
    },
    3: {
        'id': 3,
        'title': 'Cat',
        'content': 'This is a picture of a cat.',
        'date_posted': 'June 15th 2020',
        'date_updated': 'June 16th 2020',
        'history': {'June 15th 2020', 'June 16th 2020'},
    },
    4: {
        'id': 4,
        'title': 'Russian Blue Cat',
        'content': 'This is a picture of a Russian Blue cat.',
        'date_posted': 'June 15th 2020',
        'date_updated': 'June 16th 2020',
        'history': {'June 15th 2020', 'June 16th 2020'},
    },
}


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
    ordering = ['-date_updated']


class WikiDetailView(DetailView):
    model = Content


def dummy_list_view(request):
    context = {
        'dummy_data': dummy_data,
        }

    return render(request, "wiki/dummy_data_list.html", context)


def dummy_view(request, id):
    context = {
        'dummy_data': dummy_data[id],
        }

    return render(request, "wiki/dummy_data.html", context)


def dummy_edit_history(request, id):
    context = {
        'dummy_data': dummy_data[id],
        }

    return render(request, "wiki/dummy_edits.html", context)


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
