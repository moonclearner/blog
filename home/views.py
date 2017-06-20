from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from models import Article
from models import Category
from .forms import ArticleForm
from django.http import Http404
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from django.shortcuts import render_to_response
import markdown2
from django.views.decorators.cache import cache_page
import cache_manage
import pdb


# Create your views here.

@cache_page(60 * 15)
def blog(request):
    postsAll = Article.objects.filter(published_date__isnull=False).order_by('-published_date')
    paginator = Paginator(postsAll, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
        #  for i in posts:
        #      i.text = markdown2.markdown(i.text, extras=["fenced-code-blocks", "toc", "numbering", "footnotes", "cuddled-lists"])
    return render(request, 'blog/blog.html', {'posts': posts, 'page': True})


@cache_page(60 * 15)
def detail(request, pk):
    """docstring for post_detail"""
    post = get_object_or_404(Article, pk=pk)
    #  post.text = markdown2.markdown(post.text, extras=["fenced-code-blocks", "toc", "numbering", "footnotes", "cuddled-lists"])
    #  cache_manage.update_click(post)
    post.increase_click()
    return render(request, 'blog/detail.html', {'post': post})


@login_required
def writing(request):
    """docstring for post_new"""
    if request.is_ajax():
        if request.method == 'POST':
            return HttpResponse(markdown2.markdown(request.POST.get('text'), extras=["fenced-code-blocks", "toc", "numbering", "footnotes", "cuddled-lists"]))
    elif request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            if request.POST['tag']:
                # before add need clear all, avoid unique constraint
                post.tag.clear()
                for i in request.POST.getlist('tag'):
                    # get only get last one of attr
                    post.tag.add(i)
            return redirect('detail', pk=post.pk)
    else:
        form = ArticleForm()
    return render(request, 'blog/writing.html', {'form': form})


# if not auth will redirect to login
@login_required(redirect_field_name='login')
def draft_list(request):
    """docstring for post_draft_list"""
    posts = Article.objects.filter(published_date__isnull=True).order_by('-created_date')
    return render(request, 'blog/draft_list.html', {'posts': posts})


@login_required
def publish(request, pk):
    post = get_object_or_404(Article, pk=pk)
    # Article model has publish function to save published_date
    post.publish()
    return redirect('detail', pk=pk)


@login_required
def modification(request, pk):
    post = get_object_or_404(Article, pk=pk)
    if request.is_ajax():
        if request.method == 'POST':
            return HttpResponse(markdown2.markdown(request.POST.get('text'), extras=["fenced-code-blocks", "toc", "numbering", "footnotes", "cuddled-lists"]))
    elif request.method == "POST":
        # instance attr post is instance object
        form = ArticleForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            if request.POST['tag']:
                # before add need clear all, avoid unique constraint
                post.tag.clear()
                for i in request.POST.getlist('tag'):
                    # get only get last one of attr
                    post.tag.add(i)
            return redirect('detail', pk=post.pk)
    else:
        form = ArticleForm(instance=post)
    return render(request, 'blog/writing.html', {'form': form})


def get_object_or_None(klass, *args, **kwargs):
    """
    Uses get() to return an object, or None if the object does not exist.
    """
    try:
        return klass.objects.get(*args, **kwargs)
    except klass.DoesNotExist:
        return None


@login_required
def remove(request, pk):
    post = get_object_or_404(Article, pk=pk)
    category = Category.objects.get(name=post.category)
    lastarticle = get_object_or_None(Article, pk=post.lastarticle)
    nextarticle = get_object_or_None(Article, pk=post.nextarticle)
    if lastarticle is not None and nextarticle is not None:
        lastarticle.nextarticle = nextarticle.pk
        nextarticle.lastarticle = lastarticle.pk
        lastarticle.save()
        nextarticle.save()
    elif nextarticle is None and lastarticle is not None:
        lastarticle.nextarticle = None
        category.newarticle = lastarticle.pk
        lastarticle.save()
        category.save()
    else:
        category.newarticle = None
        category.save()
    post.delete()
    return redirect('blog')


@cache_page(60 * 15)
def search_condition(request, condition, mode):
    if mode == 'article':
        # one to many have two methods to search
        postsAll = Category.objects.get(pk=condition).article_set.all().filter(published_date__isnull=False).order_by('-published_date')
        #  postsAll = Article.objects.filter(category__name__exact=condition).filter(published_date__isnull=False).order_by('-published_date')
    elif mode == 'author':
        postsAll = Article.objects.filter(author__pk__exact=condition).filter(published_date__isnull=False).order_by('-published_date')
    elif mode == 'tag':
        postsAll = Article.objects.filter(tag__pk__exact=condition).filter(published_date__isnull=False).order_by('-published_date')
    elif mode == 'times':
        if len(condition) == 4:
            postsAll = Article.objects.filter(published_date__year=condition).filter(published_date__isnull=False).order_by('-published_date')
        elif len(condition) == 6:
            postsAll = Article.objects.filter(published_date__year=str(condition)[0:4]).filter(published_date__month=str(condition)[4:]).order_by('-published_date')
        elif len(condition) == 8:
            postsAll = Article.objects.filter(published_date__year=str(condition)[0:4]).filter(published_date__month=str(condition)[4:6]).filter(published_date__day=str(condition)[6:8]).order_by('-published_date')
    paginator = Paginator(postsAll, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/blog.html', {'posts': posts, 'page': True})


def about_me(request):
    return render(request, 'blog/about_me.html')


@cache_page(60 * 15)
def blog_search(request, searchcontent):
    if searchcontent is None:
        return render(request, 'blog/blog.html')
    else:
        # there has two underline
        post_list = Article.objects.filter(title__icontains=searchcontent).filter(published_date__isnull=False)
        # QuerySet merge use |
        post_list |= Article.objects.filter(text__icontains=searchcontent).filter(published_date__isnull=False)
        paginator = Paginator(post_list, 5)
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        return render_to_response('blog/blog.html', {'posts': posts, 'page': True})


@cache_page(60 * 15)
def index(request):
    """docstring for index"""
    categories = Category.objects.all()
    return render(request, 'blog/index.html', {'categories': categories})


@login_required
def uploadfiletomarkdown(request):
    if request.is_ajax():
        if request.method == 'POST':
            return HttpResponse(markdown2.markdown(request.POST.get('text'), extras=["fenced-code-blocks", "toc", "numbering", "footnotes", "cuddled-lists"]))
