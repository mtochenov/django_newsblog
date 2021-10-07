from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView, ListView


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/news_details.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news_delete.html'
    context_object_name = 'article'


def news_create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была некорректно заполнена'

    form = ArticlesForm()
    data = {
        'title': 'Добавить новость',
        'form': form,
        'error': error,
    }
    return render(request, 'news/create.html', data)


class NewsListView(ListView):
    model = Articles
    paginate_by = 2
    template_name = 'news/news_home.html'
    context_object_name = 'articles'
    ordering = ['-id']


# def news_home(request):  # Ранее новости выводились через эту функцию
#     news = Articles.objects.order_by('-id')
#     data = {
#         'title': 'Новости',
#         'news': news
#     }
#     return render(request, 'news/news_home.html', data)
