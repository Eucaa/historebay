from django.shortcuts import render, get_object_or_404
from .models import Category
from products.models import Product


def show_category(request, categoryList=None):
    """Show a list of all available categories"""
    category_slug = categoryList.split('/')
    category_queryset = list(Category.objects.all())
    all_slugs = [x.slug for x in category_queryset]
    parent = None
    for slug in category_slug:
        if slug in all_slugs:
            parent = get_object_or_404(Category, slug=slug, parent=parent)
        else:
            instance = get_object_or_404(Product, slug=slug)
            return render(request, "products.html", {'instance': instance})

    return render(request, "categories.html",
                  {'products_set': parent.products_set.all(),
                   'sub_categories': parent.children.all()})
