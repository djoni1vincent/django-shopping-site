from django.shortcuts import render
from django.views import generic

from .models import Brand, Category, Product

# Create your views here.


def index(request):
    """View function for home page of site."""
    num_products = Product.objects.all().count()
    categories = Category.objects.all()
    brands = Brand.objects.all()

    context = {
        "num_products": num_products,
        "categories": categories,
        "brands": brands,
    }

    return render(request, "catalog/index.html", context=context)


class ProductListView(generic.ListView):
    model = Product
    context_object_name = "product_list"


class ProductDetailView(generic.DetailView):
    model = Product
    context_object_name = "product_detail"
