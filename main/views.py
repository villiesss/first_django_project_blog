from django.shortcuts import render
from .models import Post

# Create your views here.

menu = [{"title" : "Посты", "url_name" : "main:post_list"}, 
        #{"title" : "Добавить пост", "url_name" : "main:post_add"},
        #{"title" : "О сайте", "url_name" : "main:about"},
        #{"title" : "Контакты", "url_name" : "main:contacts"},
        ]

def index_root(request):
    return render(request, 'main/index.html')


def index(request):
    return render(request, 'main/index.html')

# отображения списка постов
def post_list(request):
    # получаем все обьекты таблицы(модели) Post
    posts = Post.objects.all()
    # Заносим их в обьект контекста для передачи в шаблон
    context = {'posts': posts, 'menu': menu}
    return render(request, template_name= 'main/post_list.html', context=context)

def about_site(request):
    pass