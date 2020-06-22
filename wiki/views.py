from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Content
from django.urls import reverse
from django.db.models import Q
from .forms import ContentModelForm


dummy_data = {
    1: {
        'id': 1,
        'title': 'Fox',
        'content': 'This is dummy data that is not editable in this demo, but anyone is encouraged to create wiki posts which can also be edited by anyone. Typically a user can create, edit, and delete posts without making a profile. When clicking on a specific wiki post, links via the sidebar will automaically be made based on the title of each post.',
        'date_posted': 'June 13th 2020',
        'date_updated': 'June 14th 2020',
        'history': {'June 13th 2020', 'June 14th 2020'},
        'image': 'https://imagehost.imageupload.net/2020/06/21/fox.jpg'
    },
    2: {
        'id': 2,
        'title': 'Frog',
        'content': 'While this data on this page is static and is populated from seeded JSON data, the wiki posts from the main page that users can create will be stored in a Postgres database within the Django / Heroku backend. Pictues from this dummy data are linked from a 3rd part upload site called Imageupload.net. I had trouble with static files when this app uploaded to Heroku even when debug mode was set to false, as the images were working properly on my local machine. All pictures that are uploaded to the main site are stored via AWS S3.',
        'date_posted': 'June 12th 2020',
        'date_updated': 'June 13th 2020',
        'history': {'June 12th 2020', 'June 13th 2020'},
        'image': 'https://imagehost.imageupload.net/2020/06/21/frog.jpg'
    },
    3: {
        'id': 3,
        'title': 'Cat',
        'content': 'I have added a module for Django called Summernote which allows markdown text and other features when editing wiki posts. I thought this would be more interesting to incorporate. Another module I used was Simple-history which displays a list of every time each wiki post was updated. Click on the \'Edit History\' tab on the side bar of each wiki post to see it.',
        'date_posted': 'June 11th 2020',
        'date_updated': 'June 12th 2020',
        'history': {'June 11th 2020', 'June 12th 2020'},
        'image': 'https://imagehost.imageupload.net/2020/06/21/cat.jpg'
    },
    4: {
        'id': 4,
        'title': 'Russian Blue Cat',
        'content': 'There is search functionality which searches the title of the Content model to see if it matches any critera. Go ahead and try it out in the main part of this site.',
        'date_posted': 'June 10th 2020',
        'date_updated': 'June 11th 2020',
        'history': {'June 10th 2020', 'June 11th 2020'},
        'image': 'https://imagehost.imageupload.net/2020/06/21/russian_blue_cat.jpg'
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


class WikiListView(ListView):
    model = Content
    template_name = 'wiki/home.html'
    context_object_name = 'contents'
    ordering = ['-date_updated']
    paginate_by = 4


class WikiResultsView(ListView):
    model = Content
    template_name = 'wiki/results.html'


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


class WikiDeleteView(DeleteView):
    model = Content
    template_name = 'wiki/content_delete.html'

    def get_success_url(self):
        return reverse("wiki-home")


class WikiEditsView(DetailView):
    model = Content
    template_name = 'wiki/edits.html'

    def get_success_url(self):
        return reverse("wiki-details", kwargs={"pk": self.object.id})


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
