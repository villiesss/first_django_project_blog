from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.http import HttpResponsePermanentRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

menu = [{"title" : "Посты", "url_name" : "main:post_list"}, 
        {"title" : "Добавить пост", "url_name" : "main:post_add"},
        {"title" : "О сайте", "url_name" : "main:about"},
        {"title" : "Контакты", "url_name" : "main:contacts"},
        ]
# Main page 
def index_root(request):
    return HttpResponsePermanentRedirect("/blog/posts")
# Main page of main app
def index(request):
    return HttpResponsePermanentRedirect("/blog/posts")

def about(request):
    title = "О сайте"
    context = {"title": title, "menu": menu}
    return render(request, 'main/about.html', context=context)

def contacts(request):
    title = "Контакты"
    context = {"title": title, "menu": menu}
    return render(request, 'main/contacts.html', context=context)

# отображения списка постов
def post_list(request):
    # получаем все обьекты таблицы(модели) Post
    posts = Post.objects.all()
    # Заносим их в обьект контекста для передачи в шаблон
    context = {'posts': posts, 'menu': menu}
    return render(request, template_name= 'main/post_list.html', context=context)

@login_required
def post_add(request):
    title = "Create Post"
    if request.method == "GET":
        form = PostForm()
        context = {"title": title, "menu": menu, "form": form}
        return render(request, "main/post_add.html", context)
    
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = Post()
            post.author = request.user
            post.title = post_form.cleaned_data['title']
            post.text = post_form.cleaned_data['text']
            post.image = post_form.cleaned_data['image']
            post.publish()
            return post_list(request)
 
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    title = "Информация о посте"
    context = {"post": post, "title": title, "menu":menu}
    return render(request, template_name="main/post_detail.html", context=context)


def post_update(request, pk):
    post = Post.objects.get(pk=pk)
    title = "Изменить пост"

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("main:post_detail", pk=pk)
        
    form = PostForm(instance=post)
    return render(request, "main/post_update.html", context={"form": form, "title":title, "menu": menu})


def post_delete(request, pk):
    post = Post.objects.filter(pk=pk).first()

    if request.method == "POST":
        if "delete" in request.POST:
            post.delete()
            return redirect("main:post_list")
        if "cancel" in request.POST:
            return redirect("main:post_list")

    
    form = PostForm(instance=post)
    return render(request, "main/post_delete.html", {"form": form, "menu": menu, "post":post})


