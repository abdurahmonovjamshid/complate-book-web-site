from .forms import BookSearchForm
from .models import Category


def category_links(request):
    category = Category.objects.all()
    return {'categories': category}


def book_search(request):
    search_from = BookSearchForm
    if request.method == 'POST':
        search_from = BookSearchForm(request.POST)
        if search_from.is_valid():
            search_from.save()
    return {'search_from': search_from}
