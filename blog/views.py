from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Author, Blog, Comment


class HomePageView(generic.TemplateView):
    template_name = 'index.html'

def index(request):
    return render(request, 'index.html')

class BlogListView(generic.ListView):
    model = Blog

class BlogDetailView(generic.DetailView):
    model = Blog

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author

def author_detail_view(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    return render(request, 'author_detail.html', {'author': author})