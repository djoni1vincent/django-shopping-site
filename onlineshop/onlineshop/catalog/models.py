from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.urls import reverse


class Product(models.Model):
    """Model for products"""

    name = models.CharField(max_length=100, help_text="Enter a name of the product")
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE, null=False)
    price = models.DecimalField(
        help_text="Enter a price for the product", decimal_places=2, max_digits=10
    )
    stock = models.PositiveIntegerField()
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(
        "Category", on_delete=models.PROTECT, related_name="products"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["-created_at"]

    def __str__(self):
        """String for reprasentating Model object"""
        return f"{self.name}"


class Category(models.Model):
    """Model for Category"""

    name = models.CharField(
        max_length=100,
        verbose_name="Title",
        unique=True,
        help_text="Enter a catagory name (Electonic, Cables, etc.)",
    )

    def __str__(self):
        """String for reprasentating Model object"""
        return f"{self.name}"

    def get_absolute_url(self):
        """Returns the url to access particular category instance."""
        return reverse("category-detail", args=[str(self.id)])

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

        constraints = [
            UniqueConstraint(
                Lower("name"),
                name="category_name_case_insensitive",
                violation_error_message="Category already exists (case insensitive match)",
            )
        ]


class Brand(models.Model):
    """Model for Brands"""

    name = models.CharField(
        max_length=100,
        verbose_name="Title",
        unique=True,
        help_text="Enter a brand name (Apple, Samsung, etc.)",
    )

    def __str__(self):
        """String for reprasentating Model object"""
        return f"{self.name}"

    def get_absolute_url(self):
        """Returns the url to access particular brand instance."""
        return reverse("brand-detail", args=[str(self.id)])

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

        constraints = [
            UniqueConstraint(
                Lower("name"),
                name="brand_name_case_insensitive",
                violation_error_message="Brand already exists (case insensitive match)",
            )
        ]
