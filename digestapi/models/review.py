from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Review(models.Model):
    book = models.ForeignKey(
        "Book", on_delete=models.CASCADE, related_name="book_review"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews_created"
    )
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    comment = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
