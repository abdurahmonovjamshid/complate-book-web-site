from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.shortcuts import redirect, render

from .forms import CreateUserForm
from .models import Book, Category


# Create your views here.
def home(request):
    recommended_books = Book.objects.filter(recomended_books=True)
    fiction_books = Book.objects.filter(fiction_books=True)
    business_books = Book.objects.filter(business_books=True)

    return render(request, 'home.html', {
        'recommended_books': recommended_books,
        'fiction_books': fiction_books,
        'business_books': business_books})


def all_books(request):
    books = Book.objects.all()
    return render(request, 'all_books.html', {'books': books})


def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    return render(request, 'ganre_detail.html', {'ganre': category})

@login_required(login_url='login')
def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    cats = book.category.all()
    similar_books_list = [[book]]
    for cat in cats:
        similar_books_list.append(cat.books.all().exclude(slug=book.slug))
    return render(request, 'book_detail.html', {
        'book': book,
        'similar_books_list': similar_books_list})


def search_book(request):
    query = ''
    if request.POST.get('name_of_book'):
        query = request.POST.get('name_of_book')
    # filtered_cat = Q(category__in=Category.objects.filter(name__icontains=query))
    search_books = Book.objects.filter(
        Q(title__icontains=query) | Q(summary__icontains=query))
    return render(request, 'search_book.html', {'search_books': search_books})


def register_page(request):
    register_form = CreateUserForm()
    if request.method == 'POST':
        register_form = CreateUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.info(request, 'Account created succesfuly! Login')
            return redirect('login')
    return render(request, 'register.html', {'signup_form':register_form})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Invalid Credentials")
    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    return redirect('home')