from django.shortcuts import render



def book1(request):
    """
    render the book1 page
    """
    return render(request, 'book1/book.html')
# Create your views here.
