from django.contrib.sessions.models import Session
from django.shortcuts import render
from django.template.context_processors import request
from django.views import generic

from .models import Brand, Category, Product

# Create your views here.


def index(request):
    """View function for home page of site."""
    num_products = Product.objects.all().count()
    categories = Category.objects.all()
    brands = Brand.objects.all()

    num_visits = request.session.get("num_visits", 0)
    num_visits += 1
    request.session["num_visits"] = num_visits

    context = {
        "num_products": num_products,
        "categories": categories,
        "brands": brands,
        "num_visits": num_visits,
    }

    return render(request, "catalog/index.html", context=context)


class ProductListView(generic.ListView):
    model = Product
    paginate_by = 5
    context_object_name = "product_list"


class ProductDetailView(generic.DetailView):
    model = Product
    context_object_name = "product_detail"


class BrandListView(generic.ListView):
    model = Brand
    context_object_name = "brand_list"


class BrandDetailView(generic.DetailView):
    model = Brand
    context_object_name = "brand_detail"
