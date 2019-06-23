import datetime
from django.shortcuts import render
from django.views import generic

from blogsite.models import Blogger, BlogPost
# Create your views here.

def index(request):
    """View function for homepage of site"""

    num_posts = BlogPost.objects.all().count()
    num_bloggers = Blogger.objects.all().count()
    latest_blog = BlogPost.objects.latest('post_date')

    context = {
        'num_posts': num_posts,
        'num_bloggers': num_bloggers,
        'latest_blog': latest_blog,
    }

    return render(request, 'index.html', context=context)


class BlogPostListView(generic.ListView):
    model = BlogPost
    paginate_by = 10


class BlogPostDetailView(generic.DetailView):
    model = BlogPost