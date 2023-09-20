from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

# カテゴリモデル
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

# オークションリストモデル
class AuctionListing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_bid = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')  # sellerの逆参照名を'listings'に設定
    closed = models.BooleanField(default=False)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='won_listings')  # winnerの逆参照名を'won_listings'に設定

    def __str__(self):
        return self.title


# 入札モデル
class Bid(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)

# ウォッチリストモデル
class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listings = models.ManyToManyField(AuctionListing)

# コメントモデル
class Comment(models.Model):
    text = models.TextField()
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

