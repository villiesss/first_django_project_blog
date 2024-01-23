from django.shortcuts import render
from .models import Post
from .forms import PostForm

# Create your views here.

menu = [{"title" : "Посты", "url_name" : "main:post_list"}, 
        {"title" : "Добавить пост", "url_name" : "main:post_add"},
        {"title" : "О сайте", "url_name" : "main:about"},
        {"title" : "Контакты", "url_name" : "main:contacts"},
        ]
# Main page 
def index_root(request):
    return render(request, 'main/index_root.html')

# Main page of main app
def index(request):
    return render(request, 'main/index.html', context={"menu" : menu})

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

# отображения списка постов
def post_list(request):
    # получаем все обьекты таблицы(модели) Post
    posts = Post.objects.all()
    # Заносим их в обьект контекста для передачи в шаблон
    context = {'posts': posts, 'menu': menu}
    return render(request, template_name= 'main/post_list.html', context=context)


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
            post.author = post_form.cleaned_data['author']
            post.title = post_form.cleaned_data['title']
            post.text = post_form.cleaned_data['text']
            post.image = post_form.cleaned_data['image']
            post.save()
            return post_list(request)
 
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    title = "Информация о посте"
    context = {"post": post, "title": title, "menu":menu}
    return render(request, template_name="main/post_detail.html", context=context)