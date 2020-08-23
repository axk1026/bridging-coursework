from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from .models import CV
from .forms import CVForm
from .models import CV2
from .forms import CV2Form
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

def homePage(request):
    return render(request, 'blog/homePage.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts' : posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def CV_list (request):
    cvs = CV.objects.all()
    return render(request, 'blog/CV_list.html', {'cvs': cvs })

def CV_detail(request, pk):
    cv = get_object_or_404(CV, pk=pk)
    return render(request, 'blog/CV_detail.html', {'cv': cv})

def CV_edit(request, pk):
    cv = get_object_or_404(CV2, pk=pk)
    if request.method == "POST":
        form = CV2Form(request.POST, instance=cv)
        if form.is_valid():
            cv = form.save(commit=False)
            cv.published_date = timezone.now()
            cv.save()
            return redirect('CV2_detail', pk=cv.pk)
    else:
        form = CV2Form(instance=cv)
    return render(request, 'blog/CV_edit.html', {'form': form})

def CV2_list (request):
    cvs = CV2.objects.all()
    return render(request, 'blog/CV2_list.html', {'cvs': cvs })

def CV2_detail(request, pk):
    cv = get_object_or_404(CV2, pk=pk)
    return render(request, 'blog/CV2_detail.html', {'cv': cv})

def CV_new(request):
    if request.method == "POST":
        form = CV2Form(request.POST)
        if form.is_valid():
            cv = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('CV2_detail', pk=cv.pk)
    else:
        form = CV2Form()
    return render(request, 'blog/CV_edit.html', {'form': form})

#it uses the template of the list items we used in the tesing goat book
#this is used to test weather i am able to use the url and save a post from that url
#and view all the posts in that url this helpped me create the above cv views and models
#that you see in these files I also used the post example we got from django girls to also help me
#create the CV builder.
# Create your views here.
