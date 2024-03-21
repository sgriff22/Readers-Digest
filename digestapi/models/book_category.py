from django.db import models
from django.contrib.auth.models import User


class BookCategory(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="books")
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="categories"
    )
    date_created = models.DateTimeField(auto_now_add=True)
