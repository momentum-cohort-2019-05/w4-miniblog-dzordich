from django.contrib.auth import get_user
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from blogsite.models import Blogger, BlogPost, Comment
from blogsite.forms import CommentForm
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


class BloggerListView(generic.ListView):
    model = Blogger

class BloggerDetailView(generic.DetailView):
    model = Blogger

@permission_required('blogsite.can_comment')
def add_comment(request, pk):
    blogpost = get_object_or_404(BlogPost, pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment.objects.create(content=form.cleaned_data['user_comment'], commenter=get_user(request), post=blogpost)
            comment.save()

            return HttpResponseRedirect(reverse('index'))

    # If this is a GET (or any other method) create the default form.
    else:
        form = CommentForm()

    context = {
        'form': form,
        'blogpost': blogpost,
    }

    return render(request, 'blogsite/add_comment.html', context)
