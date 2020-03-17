from django.shortcuts import render
from products.models import Product
# Create your models here.


def search_filter(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])  # filter() is a built-in function from Django. name__icontains works like the SQL: SELECT...WHERE name ILIKE etc..
                                                                         # The form to filter for items is called 'q' (this time). 
                                                                         # Whatever you type into it will be used to filter for matching products.
    return render(request, "products.html", {'products': products})
