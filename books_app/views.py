from django.shortcuts import render, get_object_or_404

from books_app.models import Books, Category, Author


# Create your views here.
def books_list(request):
   books_list=Books.objects.filter(status=Books.Status.Published)
   # Usuli digar
   #books_list=Books.published.all()
   context={
        "books_list": books_list,
    }
   return render(request, 'books/books_list.html',context)

def books_detail(request, id):
    books=get_object_or_404(Books,id=id,status=Books.Status.Published)
    context={
        "books": books
    }
    return render(request, 'books/books_detail.html',context)


def HomePageView(request):
    books = Books.objects.filter(status=Books.Status.Published)
    #categories=Category.objects.all()
    #authors=Author.objects.all()
    context={
        "books": books,
     #   "categories":categories,
      #  "authors":authors
    }
    return render(request, 'books/home.html', context)
def contactPageView(request):
    context={}
    return render(request,'books/contact.html', context )
def previewPageView(request,id):
    book = get_object_or_404(Books, id=id, status=Books.Status.Published)
    context = {
        "book": book
    }
    return render(request,'books/preview.html', context )