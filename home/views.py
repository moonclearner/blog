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
import pdb


# Create your views here.


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


@login_required
def detail(request, pk):
    """docstring for post_detail"""
    post = get_object_or_404(Article, pk=pk)
    #  post.text = markdown2.markdown(post.text, extras=["fenced-code-blocks", "toc", "numbering", "footnotes", "cuddled-lists"])
    post.increase_click()
    return render(request, 'blog/detail.html', {'post': post})


@login_required
def writing(request):
    """docstring for post_new"""
    #  if request.is_ajax()
    #      form = ArticleForm()
    #      if request.method == 'POST':
    #          pdb.set_trace()
    #          data = json.loads(request.body.decode('utf-8'))
    #          form.title = data['title']
    #          form.text = data['text']
    #          form.author = request.user
    #          form.save()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
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


def publish(request, pk):
    post = get_object_or_404(Article, pk=pk)
    # Article model has publish function to save published_date
    post.publish()
    return redirect('detail', pk=pk)


def modification(request, pk):
    post = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        # instance attr post is instance object
        form = ArticleForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
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


def search_condition(request, condition, mode):
    if mode == 'article':
        # one to many have two methods to search
        postsAll = Category.objects.get(name=condition).article_set.all().filter(published_date__isnull=False).order_by('-published_date')
        #  postsAll = Article.objects.filter(category__name__exact=condition).filter(published_date__isnull=False).order_by('-published_date')
    elif mode == 'author':
        postsAll = Article.objects.filter(author__username__exact=condition).filter(published_date__isnull=False).order_by('-published_date')
    elif mode == 'tag':
        postsAll = Article.objects.filter(tag__name__exact=condition).filter(published_date__isnull=False).order_by('-published_date')
    elif mode == 'times':
        postsAll = Article.objects.filter(published_date__year=condition).filter(published_date__isnull=False).order_by('-published_date')
    paginator = Paginator(postsAll, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/blog.html', {'posts': posts, 'page': True})


def archives(request):
    try:
        post_list = Article.objects.filter(published_date__isnull=False).order_by('-published_date')
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'blog/archives.html', {'post_list': post_list, 'error': False})


def about_me(request):
    return render(request, 'blog/about_me.html')


def blog_search(request):
    if 'searchcontent' in request.GET:
        searchcontent = request.GET['searchcontent']
        if searchcontent is None:
            return render(request, 'blog/post_list.html')
        else:
            # there has two underline
            post_list = Article.objects.filter(title__icontains=searchcontent)
            if len(post_list) == 0:
                errorinf = True
            else:
                errorinf = False
            return render(request, 'blog/search.html', {'post_list': post_list, 'error': errorinf})


def index(request):
    """docstring for index"""
    categories = Category.objects.all()
    return render(request, 'blog/index.html', {'categories': categories})


def work(request):
    return render(request, 'blog/work.html')
