from django.shortcuts import render

from .models import Category, Product

# Create your views here.


def index(request):
    """View function for home page of site."""
    num_products = Product.objects.all().count()
    categories = Category.objects.all()

    context = {
        "num_products": num_products,
        "categories": categories,
    }

    return render(request, "catalog/index.html", context=context)
