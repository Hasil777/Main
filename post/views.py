from django.shortcuts import render
from .forms import UserRegistrationForm
from .models import Post, Comment
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST
from django.contrib.postgres.search import SearchVector
from .forms import SearchForm
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.decorators import login_required
import sys
def home(request):
    return render(request,'post/home.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user= user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password2']
            )
            new_user.save()
            context = {
                'new_user':new_user
            }
            return render(
                request=request,
                template_name='post/register_done.html',
                context=context
            )
    else:
        user_form = UserRegistrationForm()
    context={
        'user_form':user_form
    }
    return render(request=request,template_name='post/register.html',context=context)
@login_required 
def post_detail(request,post):
    # Old version
    '''
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404('No post found')
    '''
    
    post = get_object_or_404(
        Post,  
        slug=post,
    )

    '''comments = post.comments.filter(active=True)
    form = CommentForm()'''

    context = {
        'post': post,
        #'comments': comments,
        #'form': form
    }

    return render(
        request,
        'post/detail.html',
        context
    )

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(get_absolute_url)
            subject = f"{cd['name']} recommends your read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n {cd['name']}'s comments: {cd['comments']}"
            
            send_mail(
                subject,
                message,
                'atabekdemurtaza@gmail.com',
                [cd['to']],   
            )
            sent = True
    
    else:
        form = EmailPostForm()
    
    context = {
        'post': post,
        'form': form,
        'sent': sent
    }

    return render(request, 'post/share.html', context)



def post_comment(request, post_id):
    post = get_object_or_404(Post, slug=post_id)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    
    context = {
        'post': post,
        'comment': comment,
        'form': form,
    }

    return render(request, 'post/blog/includes/comment.html', context)


def post_search(request):
    form = SearchForm()
    query = None
    results = list()

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.published.annotate(
                search=SearchVector('title','body'),
        
            ).filter(search=query)
    
    context = {
        'form': form,
        'query': query,
        'results':results
    }

    return render(request, 'post/search.html', context)

def movies(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(
        request=request,
        template_name='post/dashboard.html',
        context=context
    )